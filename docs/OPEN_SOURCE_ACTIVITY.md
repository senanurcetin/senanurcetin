# Open-source contribution and maintainer activity

**Account:** [@senanurcetin](https://github.com/senanurcetin)  
**Historical GitHub search snapshot:** 2026-10-27 (UTC); **merged-PR metadata recheck:** 2026-10-30 (UTC)  
**Scope:** GitHub pull requests authored by this account in repositories **not owned by** `senanurcetin`. Counts are dated evidence, not live program eligibility or current CI results.

## Reproducible inventory

On **27 October 2026**, GitHub's pull-request search returned **52 third-party PRs**: **14 merged**, **30 open**, and **8 closed without merge**. These three counts are a **historical snapshot**, not current totals after the additional merge on 28 October. Repository ownership, not the fork's remote origin or an author's own fork, determines whether a PR is external. PRs in `senanurcetin/*` are excluded.

- [All 52 third-party PRs — live GitHub query](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+-user%3Asenanurcetin&type=pullrequests)
- [Merged third-party PRs — live query (14 at 27 Oct snapshot)](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Amerged+-user%3Asenanurcetin&type=pullrequests)
- [Open third-party PRs — live query (30 at 27 Oct snapshot)](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Aopen+-user%3Asenanurcetin&type=pullrequests)
- [Last-12-month merged-PR filter](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Amerged+merged%3A%3E%3D2025-10-27+-user%3Asenanurcetin&type=pullrequests)

GitHub search counts can change after this snapshot. Any support/funding application must check individual merges and rerun the live queries on the submission date; this document is **not** an eligibility certificate.

### Reproducible local verification (no tokens)

The repository includes a dependency-free [Node.js auditor](../scripts/audit-external-prs.mjs) with [offline regression tests](../tests/audit-external-prs.test.mjs). It reads **GitHub's public search API only**, excludes PRs to repositories owned by this account, uses a strict UTC merge-date cutoff, checks the search result count and refuses incomplete/duplicate/untrusted records. GitHub anonymous API rate limits apply. Run locally from the profile repository root:

```sh
node --test tests/audit-external-prs.test.mjs
node scripts/audit-external-prs.mjs --since 2025-10-26
```

**26 October 2026 refreshed verification:** Windows / Node.js v24.13.0: **6/6 auditor tests passed**. A single live read-only GitHub search produced **51 external PRs: 13 merged, 30 open, 8 closed without merge**; all 13 merges were within the requested date window. No GitHub Actions jobs were triggered and no GitHub access token was needed. The script produces a runtime snapshot and does not verify GitHub program membership, downloads, external adoption or review approvals.

**27 October 2026 refreshed inventory:** GitHub's live public search returned **52 external PRs: 14 merged, 30 open, 8 closed without merge**. [Xarray #11806](https://github.com/pydata/xarray/pull/11806) was independently confirmed merged at **2026-10-27 09:54:42 UTC**, merge commit [`5923b17`](https://github.com/pydata/xarray/commit/5923b1794c2e2b781bcd3d91c9f21aa121c6a65a). Earlier 26 October counts above remain historical evidence, not the current snapshot. [hvPlot #1767](https://github.com/holoviz/hvplot/pull/1767) is now an **open external PR**; it does not change the 14 merged count.

**30 October 2026 PR-detail recheck:** Independently fetched the GitHub PR detail endpoints for the **15 specific merged third-party PRs** listed below. All 15 had `merged=true`, author `senanurcetin`, and an exact matching `merged_at` UTC timestamp. They span **six upstream repository owners**. The [dated receipt ledger](https://github.com/senanurcetin/nexus-devops-intelligence/blob/main/docs/OSS_MERGED_UPSTREAM_LEDGER_2026-10-30.json) and its [offline consistency validator](https://github.com/senanurcetin/nexus-devops-intelligence/blob/main/scripts/validate-oss-merge-ledger.mjs) record this evidence; this manual live check is separate from the validator, which performs no GitHub calls. The full current open/closed PR inventory was **not** recounted in this recheck. Neither the count nor a merged status establishes developer-program eligibility or downstream adoption.

## Verified third-party merged pull requests

| Upstream | Merged PR | Contribution |
| --- | --- | --- |
| pyjanitor | [#1822](https://github.com/pyjanitor-devs/pyjanitor/pull/1822) | Homogeneous NumPy `.value` fast path; **merged 28 October 2026 at 02:10:22 UTC** |
| Xarray | [#11806](https://github.com/pydata/xarray/pull/11806) | Document optional DataTree backend entrypoints; **merged 27 October 2026 at 09:54:42 UTC** |
| pyjanitor | [#1786](https://github.com/pyjanitor-devs/pyjanitor/pull/1786) | Include missingness in constant-column handling |
| pyjanitor | [#1820](https://github.com/pyjanitor-devs/pyjanitor/pull/1820) | Prevent `pivot_longer` output from mutating the source via shared buffers |
| SciPy | [#26391](https://github.com/scipy/scipy/pull/26391) | Illustrate smoothing and scaling for `make_splrep` |
| Altair | [#4178](https://github.com/vega/altair/pull/4178) | Self-contained interactive HTML documentation |
| Altair | [#4180](https://github.com/vega/altair/pull/4180) | Inline dictionary and URL source documentation |
| Plotly.py | [#5823](https://github.com/plotly/plotly.py/pull/5823) | Figure-factory return-type documentation |
| Xarray | [#11713](https://github.com/pydata/xarray/pull/11713) | `Dataset.drop_duplicates` examples |
| DuckDB documentation | [#7494](https://github.com/duckdb/duckdb-web/pull/7494) | NULL list values in `FILTER` documentation |
| DuckDB documentation | [#7495](https://github.com/duckdb/duckdb-web/pull/7495) | Window/aggregate clause-placement documentation |
| DuckDB documentation | [#7496](https://github.com/duckdb/duckdb-web/pull/7496) | Deprecated PRAGMA assignments |
| Xarray | [#11715](https://github.com/pydata/xarray/pull/11715) | Closing netCDF datasets before overwrite |
| Altair | [#4179](https://github.com/vega/altair/pull/4179) | `Chart.show()` documentation |
| Xarray | [#11714](https://github.com/pydata/xarray/pull/11714) | Expected all-NaN warning behavior |

All **15 listed** PRs were individually confirmed merged in the 12-month window **2025-10-30 through 2026-10-30** against GitHub PR detail metadata. The earlier 14-count and 27 October search dates above remain historical. This is **not** 100 merged third-party PRs.

**pyjanitor #1822 historical validation:** Before merge, fork commit [`d6b135c`](https://github.com/senanurcetin/pyjanitor/commit/d6b135cea30f60c883de99a89c5afaf44620ae66) reported **578 local passing tests, 7 expected xfails** and 32 temporal/complex/float16 regression cases. Its upstream Python CI and docs CI were reported passing. This is dated pre-merge QA, not evidence of external adoption. [Performance benchmark](benchmarks/pyjanitor-1822-2026-10-26.md) measured an earlier commit and must not be attributed to a newer version without rerunning it.

## Active upstream queue

**30 open third-party PRs at the historical 27 October snapshot.** The live queue has since changed; notably pyjanitor #1822 merged on 28 October. Examples still requiring independent upstream review include:

- [hvPlot #1767](https://github.com/holoviz/hvplot/pull/1767): categorical color grouping in line/step/area, with named index, boolean categories and default `hvplot(...)` line calls. **Open; external CI `action_required`.**
- [Anthropic Claude Agent SDK Python #1421](https://github.com/anthropics/claude-agent-sdk-python/pull/1421): transcript timestamp handling.
- [OpenAI Knowledge Retrieval #9](https://github.com/openai/openai-knowledge-retrieval/pull/9): citation-limit enforcement.
- [Vega Altair #4189](https://github.com/vega/altair/pull/4189): layering charts without local data.
- [Vega-Lite #9956](https://github.com/vega/vega-lite/pull/9956): CLI parsing/spec locale preservation.
- [Skrub #2347](https://github.com/skrub-data/skrub/pull/2347): missingness-indicator HOWTO.


### Seaborn multi-PR compatibility check (27 October 2026)

An **isolated local worktree**, not an upstream or published integration branch, combined four **open** Seaborn contributions at the shared upstream base `c1cb287835852406691aed60ea0c62710f2c6b18`:

| Upstream PR | Tested fork head | Scope |
| --- | --- | --- |
| [#4010](https://github.com/mwaskom/seaborn/pull/4010) | `fe8b2ea` | Binary numeric size mapping |
| [#4012](https://github.com/mwaskom/seaborn/pull/4012) | [`f819994`](https://github.com/senanurcetin/seaborn/commit/f819994ed5153b15596f9c1c75cc44fb6deb5630) | Weighted KDE overflow/zero-weight protection and restored support for numeric pandas `object` weight columns |
| [#4013](https://github.com/mwaskom/seaborn/pull/4013) | `62d8d1a` | Mixed numeric/text histogram categories |
| [#4022](https://github.com/mwaskom/seaborn/pull/4022) | `37c428e` | Nonzero stacked-bar baselines across facets |

All four histories **merged cleanly in the test worktree**. On Windows / Python 3.13 / Matplotlib `Agg`, the original integration checkout passed **683 tests (1 skipped)**. After applying the latest #4012 object-weight regression fix (test-only integration commit `1a489d56`, **not** pushed), the updated integration passed **707 tests (1 skipped)** across `tests/test_distributions.py`, `tests/test_base.py`, `tests/test_relational.py`, `tests/_core/test_moves.py` and `tests/_marks/test_bar.py`:

```sh
python -m pytest -q -o addopts= tests/test_distributions.py tests/test_base.py tests/test_relational.py tests/_core/test_moves.py tests/_marks/test_bar.py
```

Ruff **lint** on all modified source/test files and `git diff --check` passed. In a separate cross-feature probe on the same integrated worktree, **16 comparisons** passed for `histplot` and `displot(kind="hist")`, with/without hue and with `probability`, `proportion`, `percent` and `density` statistics: finite histogram heights from weights `1e308` matched the `1.0`-weighted output for mixed numeric/text categories. This is an interaction check for #4012 and #4013, **not** an upstream CI result. Runtime warnings from a legacy negative-weight test and a pytest deprecation warning were observed; neither caused failures.

**Regression discovery and fix on #4012 (27 October 2026):** The earlier #4012 head `0a353e3` raised `TypeError` on numeric pandas `object` weight columns because its new `np.isfinite` validation attempted to process object arrays directly; the shared upstream base accepted the same input. Commit [`f819994`](https://github.com/senanurcetin/seaborn/commit/f819994ed5153b15596f9c1c75cc44fb6deb5630) converts only object/nullable weight values for finite checks while retaining native numerical types, and adds **24 committed differential regression cases** comparing numeric-object weights against equivalent float64 weights for KDE and histogram density/probability, with/without hue and ordinary, very large, sparse or missing weights. **24 new focused tests** and the full local distributions module (**314 passed, 1 skipped**) succeeded; lint and whitespace checks passed. The updated four-PR integration also passed **707 tests** (1 skipped), as noted above. The latest upstream fork PR CI is `action_required` (restricted external PR workflows), **not a CI pass**. Upstream acceptance and merge remain pending.

No integration commit was pushed to the upstream repositories, no individual PR was merged as a result, and no fourth-party adoption is claimed. These local results are limited to the specified environment and tests; they do not establish that every downstream usage is compatible.

An open PR is a proposed change, not an accepted or deployed upstream contribution. The [18 October upstream issue/review/CI audit](OPEN_SOURCE_PR_AUDIT_2026-10-18.md) remains a **historical** diagnostic, not the current PR inventory. Respect each upstream project's contribution and AI-assistance policy; do not automate maintainer conversation where it is prohibited.

## hvPlot #1759 / PR #1767 — verified open upstream contribution (27 October 2026)

[Issue #1759](https://github.com/holoviz/hvplot/issues/1759) reported categorical `color="cat"` failing to render in line-like plots. The fix is now submitted as **[holoviz/hvplot PR #1767](https://github.com/holoviz/hvplot/pull/1767)**, with latest fork head **[`421ec70`](https://github.com/senanurcetin/hvplot/commit/421ec70dcf2be4a8cf7d4d53ddd984fbdefa09cd)**.

- Handles categorical dataframe columns, categorical named indexes and MultiIndex levels, boolean color fields, and **implicit default line plots** (`df.hvplot(x=..., y=..., color="cat")`) for Pandas/Polars eager and lazy tables. Preserves explicit `by`, literal color strings and existing numeric-field behavior.
- A Bokeh-rendering regression module contains **36 successful parametrized cases**. The original nine categorical frontend × plot-type cases fail on unmodified upstream main `3fc8075`, verifying that the tests detect the original error.
- Fresh checkout of the **exact GitHub fork commit `421ec70`**: initial `testplotting.py` plus new regressions: **130 passed, 2 skipped**; Bokeh-only options: **73 passed** (149 tests deselected). After installing the Matplotlib and Plotly optional rendering dependencies, the **combined plotting, all-backend options and regression modules passed 311 tests, 23 skipped, 20 expected xfails** (Windows / Python 3.13; `matplotlib` `Agg`). Ruff lint, format and Git diff checks passed. This is an expanded selection, **not** the complete hvPlot test suite.
- Independently rendered **36/36 cross-backend combinations**: Bokeh, Matplotlib and Plotly × Pandas, Polars DataFrame and LazyFrame × `line`, `step`, `area` and implicit default `hvplot(...)` categorical grouping. The probe **asserted `hvplot.__file__` belonged to the exact PR checkout**. An initial probe accidentally loaded the older editable installation from the interpreter environment; its reported 9 default-kind failures were **test-path artifacts, not PR regressions**, and disappeared once the correct import path was enforced. No code modification was required.
- **27 October expanded independent suite, exact PR head `421ec70`:** `python -m pytest -q hvplot/tests/test_categorical_line_color.py hvplot/tests/testcharts.py hvplot/tests/testoptions.py hvplot/tests/testplotting.py hvplot/tests/plotting --disable-warnings --maxfail=1` finished with **1,030 passed, 39 skipped, 23 expected failures (`xfail`), 9 warnings, exit code 0** out of 1,092 collected tests (Windows, Python 3.13.14, pytest 9.1.1, Matplotlib `Agg`). Explicitly confirmed `hvplot.__file__` loads the PR checkout; the Git worktree was clean afterward. The initial collection attempt stopped because the isolated test environment lacked the `parameterized` package; installation and a clean rerun resolved this environment-only issue. These additional tests do **not** constitute the entire repository suite or upstream CI.
- The upstream `tests` and `zizmor` workflows report **`action_required`**, **not green CI**. PR is open, mergeable and awaiting maintainer review; no upstream acceptance or merge claimed.

## Owned-project maintenance (separate evidence)

Maintained public repositories include [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot), [NEXUS DevOps Intelligence](https://github.com/senanurcetin/nexus-devops-intelligence), [Vision2DCS](https://github.com/senanurcetin/Vision2DCS), [PlantLog-MERN](https://github.com/senanurcetin/PlantLog-MERN), and [Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics).

Their own pull requests, tests, releases, documentation and maintenance show work on **owned** repositories, but do **not** increase the external merged-PR count. Third-party usage, package downloads, downstream dependency reach and independent maintainers must be demonstrated separately. Do not interpret a green CI badge, star count, owner-authored PR, or a pre-production demo as proof of real-world ecosystem adoption.

## Verification limits and next checks

- GitHub account `created_at` was independently read from GitHub's public user API on 26 October 2026: **2026-01-07T22:01:29Z**. The account reaches two years on **7 January 2028**. That date alone does **not** determine acceptance into any developer program.
- Verify any program's **current official requirements**, geography, application form and terms immediately before applying.
- Evaluate adoption with actual traffic/install/dependent-package evidence. No externally verified installation count, package registry downloads or commercial customers are claimed here.
- Confirm author, upstream merge, license, and review status directly from the linked GitHub PR before quoting them.
- Never inflate counts by merging own PRs, generating artificial engagement, or treating `action_required` CI as a pass.

For practices and policy checks, see [the open-source contribution guide](OPEN_SOURCE_CONTRIBUTION_GUIDE.md). For separate project demonstrations and their limitations, see [the project catalog](PROJECT_CATALOG.md).
