import test from 'node:test';
import assert from 'node:assert/strict';
import {
  validateDate, classifyPulls, auditExternalPulls, reportMarkdown,
} from '../scripts/audit-external-prs.mjs';

function item(number, state = 'open', mergedAt = null, owner = 'pydata') {
  return {
    repository_url: 'https://api.github.com/repos/' + owner + '/xarray',
    number,
    state,
    html_url: 'https://github.com/' + owner + '/xarray/pull/' + number,
    pull_request: { merged_at: mergedAt },
  };
}
function api(pages, { errorStatus = null, incomplete = false, count = null } = {}) {
  const requested = [];
  const fetchImpl = async (url, opts) => {
    const parsed = new URL(url);
    assert.equal(parsed.host, 'api.github.com');
    assert.equal(parsed.pathname, '/search/issues');
    assert.equal(parsed.searchParams.get('q'),
      'is:pr author:senanurcetin -user:senanurcetin');
    assert.equal(parsed.searchParams.get('per_page'), '100');
    assert.equal(opts.headers['X-GitHub-Api-Version'], '2022-11-28');
    assert.equal(opts.method, undefined);
    const page = Number(parsed.searchParams.get('page'));
    requested.push(page);
    const list = pages[page - 1] ?? [];
    return {
      ok: !errorStatus,
      status: errorStatus || 200,
      json: async () => ({
        total_count: count ?? pages.flat().length,
        incomplete_results: incomplete,
        items: list,
      }),
    };
  };
  return { fetchImpl, requested };
}

test('date validation refuses malformed and impossible calendar dates', () => {
  assert.equal(validateDate('2025-10-26'), '2025-10-26');
  for (const value of ['2026-02-30', '2026-13-01', '2026-00-10', '2026-1-1', '',
    'today', '2025-10-26T00:00:00Z', null]) {
    assert.throws(() => validateDate(value));
  }
});

test('inventory distinguishes external merged, open and closed-unmerged with UTC cutoff', () => {
  const results = classifyPulls([
    item(1, 'closed', '2025-10-26T00:00:00Z'),
    item(2, 'closed', '2025-10-25T23:59:59Z'),
    item(3, 'open'),
    item(4, 'closed'),
  ], '2025-10-26');
  assert.deepEqual([
    results.total_external_prs, results.merged_total,
    results.merged_since_date, results.open, results.closed_without_merge,
  ], [4, 2, 1, 1, 1]);
  const rendered = reportMarkdown(results);
  assert.match(rendered, /merged since 2025-10-26/i);
  assert.match(rendered, /pydata\/xarray#1/);
  assert.doesNotMatch(rendered, /pydata\/xarray#2/);
  assert.match(rendered, /not.*proof of developer-program eligibility/i);
});

test('classifier rejects owned, spoofed, duplicate and contradictory PR records', () => {
  const bad = [
    [item(1, 'open', null, 'senanurcetin')],
    [{ ...item(1), html_url: 'https://github.com/phishing.invalid/test' }],
    [{ ...item(1), repository_url: 'https://evil.invalid/repos/a/b' }],
    [item(1), item(1)],
    [item(1, 'open', '2026-02-02T12:00:00Z')],
    [item(0)],
    [item(1, 'closed', 'not-a-date')],
  ];
  for (const records of bad) assert.throws(() => classifyPulls(records, '2025-10-26'));
});

test('merged timestamps must be real canonical UTC seconds, not normalized dates', () => {
  const good = classifyPulls([item(1, 'closed', '2024-02-29T03:04:05Z')], '2024-02-29');
  assert.equal(good.merged_since_date, 1);
  for (const mergedAt of [
    '2026-02-30T12:00:00Z', '2026-13-01T00:00:00Z',
    '2026-10-20T12:00:00.000Z', '2026-10-20T12:00:00+03:00',
    '2026-10-20T12:00:00Zjunk', '2026-10-20T25:00:00Z',
  ]) {
    assert.throws(
      () => classifyPulls([item(1, 'closed', mergedAt)], '2025-10-26'),
      /Inconsistent merged PR status/,
      mergedAt,
    );
  }
});

test('GitHub search completeness must be an explicit false boolean', async () => {
  for (const incomplete of [null, undefined, 'false', 0, true]) {
    const f = api([[item(1)]], { incomplete });
    await assert.rejects(
      auditExternalPulls({ since: '2025-10-26', fetchImpl: f.fetchImpl }),
      /incomplete or malformed/,
      String(incomplete),
    );
  }
});

test('complete two-page results are counted without overstating the merged window', async () => {
  const hundred = Array.from({ length: 100 }, (_, i) => item(i + 1));
  const apiMock = api([hundred, [item(101, 'closed', '2026-10-01T12:00:00Z')]]);
  const report = await auditExternalPulls({ since: '2025-10-26', fetchImpl: apiMock.fetchImpl });
  assert.equal(report.total_external_prs, 101);
  assert.equal(report.merged_since_date, 1);
  assert.deepEqual(apiMock.requested, [1, 2]);
});

test('empty results and one-page responses do not create unnecessary follow-up requests', async () => {
  for (const items of [[], [item(1)]]) {
    const f = api([items]);
    const report = await auditExternalPulls({ since: '2025-10-26', fetchImpl: f.fetchImpl });
    assert.equal(report.total_external_prs, items.length);
    assert.deepEqual(f.requested, [1]);
  }
});

test('failed, rate-limited, incomplete or inconsistent GitHub pages fail closed', async () => {
  const cases = [
    api([[]], { errorStatus: 403 }),
    api([[]], { incomplete: true }),
    api([[item(1)]], { count: 1001 }),
    api([[item(1)]], { count: 2 }),
    api([[item(1)], [item(2)]], { count: 101 }),
  ];
  for (const f of cases) {
    await assert.rejects(auditExternalPulls({ since: '2025-10-26', fetchImpl: f.fetchImpl }));
  }
  await assert.rejects(auditExternalPulls({
    since: '2025-10-26', fetchImpl: async () => { throw new Error('offline'); },
  }));
  await assert.rejects(auditExternalPulls({
    since: '2025-10-26',
    fetchImpl: async () => ({ ok: true, json: async () => { throw new Error('HTML'); } }),
  }));
});
