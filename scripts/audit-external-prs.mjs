#!/usr/bin/env node
/**
 * Read-only, reproducible external pull-request inventory.
 * Results are evidence, not developer-program eligibility or maintainer approval.
 */
import { pathToFileURL } from 'node:url';

const BASE = 'https://api.github.com/search/issues';
const USER = 'senanurcetin';
const MAX_RESULTS = 1000;

export function validateDate(value) {
  if (typeof value !== 'string' || !/^\d{4}-\d{2}-\d{2}$/.test(value)) {
    throw new Error('--since requires YYYY-MM-DD (UTC).');
  }
  const date = new Date(value + 'T00:00:00Z');
  if (!Number.isFinite(date.getTime()) || date.toISOString().slice(0, 10) !== value) {
    throw new Error('--since is not a valid calendar date.');
  }
  return value;
}

export function classifyPulls(items, since) {
  validateDate(since);
  const seen = new Set();
  const records = [];
  for (const item of items) {
    if (!item || typeof item !== 'object') throw new Error('Invalid GitHub item.');
    const repoMatch = /^https:\/\/api\.github\.com\/repos\/([^/]+)\/([^/]+)$/.exec(item.repository_url ?? '');
    if (!repoMatch) throw new Error('Unexpected repository URL.');
    const [, owner, repository] = repoMatch;
    if (owner.toLowerCase() === USER) throw new Error('Owned repository in an external PR query.');
    if (!Number.isSafeInteger(item.number) || item.number < 1 ||
        !['open', 'closed'].includes(item.state) ||
        item.html_url !== 'https://github.com/' + owner + '/' + repository + '/pull/' + item.number ||
        !item.pull_request || typeof item.pull_request !== 'object') {
      throw new Error('Malformed GitHub pull request.');
    }
    const key = owner.toLowerCase() + '/' + repository.toLowerCase() + '#' + item.number;
    if (seen.has(key)) throw new Error('Duplicate PR record.');
    seen.add(key);
    const merged = item.pull_request.merged_at;
    if (merged != null && (item.state !== 'closed' || typeof merged !== 'string' ||
        !Number.isFinite(Date.parse(merged)))) {
      throw new Error('Inconsistent merged PR status.');
    }
    const status = merged ? 'merged' : item.state === 'open' ? 'open' : 'closed_unmerged';
    const mergedWithinWindow = status === 'merged' &&
      Date.parse(merged) >= Date.parse(since + 'T00:00:00Z');
    records.push({
      repository: owner + '/' + repository,
      number: item.number,
      url: item.html_url,
      status,
      merged_at: merged || null,
      merged_within_window: mergedWithinWindow,
    });
  }
  const count = status => records.filter(x => x.status === status).length;
  return {
    github_user: USER,
    since_utc: since,
    total_external_prs: records.length,
    merged_total: count('merged'),
    merged_since_date: records.filter(x => x.merged_within_window).length,
    open: count('open'),
    closed_without_merge: count('closed_unmerged'),
    records: records.sort((a, b) => a.repository.localeCompare(b.repository) || a.number - b.number),
  };
}

export async function auditExternalPulls({ since, fetchImpl = fetch } = {}) {
  validateDate(since);
  const records = [];
  let expectedTotal = null;
  for (let page = 1; page <= 10; page++) {
    const params = new URLSearchParams({
      q: 'is:pr author:' + USER + ' -user:' + USER,
      per_page: '100',
      page: String(page),
    });
    let response;
    try {
      response = await fetchImpl(BASE + '?' + params, {
        headers: {
          Accept: 'application/vnd.github+json',
          'X-GitHub-Api-Version': '2022-11-28',
          'User-Agent': 'verified-oss-contribution-inventory',
        },
        signal: AbortSignal.timeout(15000),
      });
    } catch {
      throw new Error('GitHub search failed; no complete inventory was produced.');
    }
    if (!response?.ok) {
      throw new Error('GitHub search unavailable (HTTP ' + (response?.status ?? 'unknown') + ').');
    }
    let payload;
    try { payload = await response.json(); }
    catch { throw new Error('GitHub returned invalid JSON.'); }
    if (!Number.isSafeInteger(payload?.total_count) || payload.total_count < 0 ||
        !Array.isArray(payload.items) || payload.incomplete_results === true) {
      throw new Error('GitHub search result is incomplete or malformed.');
    }
    if (payload.total_count > MAX_RESULTS) {
      throw new Error('Search exceeds GitHub 1000-result limit; narrow the query.');
    }
    if (expectedTotal === null) expectedTotal = payload.total_count;
    if (expectedTotal !== payload.total_count ||
        records.length + payload.items.length > expectedTotal) {
      throw new Error('GitHub search changed during pagination; retry from scratch.');
    }
    records.push(...payload.items);
    if (records.length === expectedTotal) break;
    if (payload.items.length !== 100) throw new Error('Missing GitHub search page.');
  }
  if (records.length !== expectedTotal) throw new Error('Could not retrieve all external PR records.');
  return classifyPulls(records, since);
}

export function reportMarkdown(report) {
  const lines = [
    '# GitHub external PR evidence',
    '',
    '- Account: [@' + report.github_user + '](https://github.com/' + report.github_user + ')',
    '- External PRs observed: **' + report.total_external_prs + '**',
    '- Merged across all dates: **' + report.merged_total + '**',
    '- Merged since ' + report.since_utc + ' (UTC): **' + report.merged_since_date + '**',
    '- Open: **' + report.open + '**',
    '- Closed without merge: **' + report.closed_without_merge + '**',
    '',
    'These are GitHub search records, **not** proof of developer-program eligibility,',
    'download volumes, independent users, or current check statuses.',
    'Search counts can change between runs.',
    '',
    '## Merged external contributions in the date window',
    '',
  ];
  for (const record of report.records.filter(x => x.merged_within_window)) {
    lines.push('- [' + record.repository + '#' + record.number + '](' + record.url + ')');
  }
  return lines.join('\n') + '\n';
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    const args = process.argv.slice(2);
    if (args.length !== 2 || args[0] !== '--since') {
      throw new Error('Usage: node scripts/audit-external-prs.mjs --since YYYY-MM-DD');
    }
    const result = await auditExternalPulls({ since: args[1] });
    process.stdout.write(reportMarkdown(result));
  } catch (error) {
    console.error('Cannot verify external contributions: ' + error.message);
    process.exitCode = 1;
  }
}
