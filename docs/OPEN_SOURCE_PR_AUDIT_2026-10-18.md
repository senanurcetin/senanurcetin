# External pull request audit — 2026-10-18

Source: GitHub API snapshots of PR heads, review submissions, discussion, workflow runs, PR descriptions and linked issues. Scope: PRs authored by `senanurcetin` in **upstream repositories**, excluding PRs opened inside `senanurcetin/*` repositories. These statuses change; do not interpret this file as a live CI dashboard.

## Inventory

- **19 external PRs open** at audit time; **16 additional PRs** open in the author's own repositories (excluded).
- **SciPy #26391** was merged on **2026-10-18**, explaining why an earlier 20-external-PR working list is now 19.
- **2/19**: relevant GitHub Actions workflows successful (Altair #4178 and #4180).
- **9/19**: GitHub Actions marked `action_required` (fork-run/approval gate, NOT a test failure).
- **1/19**: mixed CI evidence (Xarray #11713: prior CI failure on a flaky network job, with other successful checks; Benchmark failure separately reported and not diagnosed).
- **7/19**: no PR-triggered Actions runs returned (all GS Quant PRs); local test claims in PR descriptions do not imply successful upstream CI.
- **1/19** had review submissions (Altair #4178: two COMMENTED reviews, both threads resolved by reviewer); 18 had no submitted reviews in the queried response.
- **12/19** directly reference validated upstream issues; **five GS Quant focused drafts** reference umbrella PR #400 rather than individual upstream issues; #399 is a DCO prerequisite and #400 is an umbrella.
- **18/19** contain explicit AI-assistance text in the PR body; DCO-only #399 does not. Disclosure presence must still be checked against each repository's requirements.

## Detailed queue

| PR | Issue relationship | Review | Hosted CI | Priority / next gate |
| --- | --- | --- | --- | --- |
| [Altair #4178](https://github.com/vega/altair/pull/4178) | [#3199](https://github.com/vega/altair/issues/3199) (open, `Closes`) | 2 comment reviews; both threads resolved | Code checks, Docs, Tests: success | P1: await maintainer decision; no outstanding inline fix found |
| [DuckDB web #7496](https://github.com/duckdb/duckdb-web/pull/7496) | [#7482](https://github.com/duckdb/duckdb-web/issues/7482) (open, `Closes`) | none | Build docs, Lint: action_required | P1: maintainer must enable checks; verify preview-only scope |
| [DuckDB web #7495](https://github.com/duckdb/duckdb-web/pull/7495) | [#7485](https://github.com/duckdb/duckdb-web/issues/7485) (open, `Closes`) | none | Build docs, Lint: action_required | P1: maintainer must enable checks |
| [GS Quant #400](https://github.com/goldmansachs/gs-quant/pull/400) | umbrella of #404–#408; no standalone issue | none | no runs found | **P0**: 40-file overlapping draft must remain non-merge-ready pending maintainer scope/merge strategy |
| [DuckDB web #7494](https://github.com/duckdb/duckdb-web/pull/7494) | [#7484](https://github.com/duckdb/duckdb-web/issues/7484) (open, `Closes`) | none | Build docs, Lint: action_required | P1: maintainer approval and docs build |
| [Xarray #11713](https://github.com/pydata/xarray/pull/11713) | [#6793](https://github.com/pydata/xarray/issues/6793) (open, `Related to`) | none | success + recorded flaky CI failure | **P0**: distinguish nonblocking PyDAP service outage from separately reported Benchmark failure; validate current head and check list before claiming CI green |
| [GS Quant #406](https://github.com/goldmansachs/gs-quant/pull/406) | focused extraction of #400 | none | no runs found | P1: current-head targeted tests stated as 15 passed; DCO #399 and scope pending |
| [Seaborn #4013](https://github.com/mwaskom/seaborn/pull/4013) | [#3846](https://github.com/mwaskom/seaborn/issues/3846) (open, `Closes`) | none | action_required | P1: maintainer CI authorization and mixed-category regression matrix |
| [Seaborn #4012](https://github.com/mwaskom/seaborn/pull/4012) | [#3817](https://github.com/mwaskom/seaborn/issues/3817) (open, `Fixes`) | none | action_required | P1: maintainer CI authorization; inspect numerical overflow/singular KDE results |
| [Seaborn #4010](https://github.com/mwaskom/seaborn/pull/4010) | [#3834](https://github.com/mwaskom/seaborn/issues/3834) (open, `Fixes`) | none | action_required | P1: maintainer CI authorization |
| [Vega-Lite #9956](https://github.com/vega/vega-lite/pull/9956) | [#9955](https://github.com/vega/vega-lite/issues/9955) (open, `Closes`) | none | Test, Check: action_required | **P0 external gate**: maintainer approval needed; prior `[skip ci]` was replaced by trigger commit; do not fake successful CI |
| [Seaborn #4011](https://github.com/mwaskom/seaborn/pull/4011) | [#2837](https://github.com/mwaskom/seaborn/issues/2837) (open, `Addresses`) | none | action_required | P1: maintainer approval |
| [Plotly #5823](https://github.com/plotly/plotly.py/pull/5823) | [#5396](https://github.com/plotly/plotly.py/issues/5396) (open, `Related to`) | none | 7 workflows: action_required | P1: maintainer approval; doc/test scope |
| [GS Quant #408](https://github.com/goldmansachs/gs-quant/pull/408) | focused extraction of #400 | none | no runs found | P1: targeted tests reported; DCO #399 and scope pending |
| [GS Quant #407](https://github.com/goldmansachs/gs-quant/pull/407) | focused extraction of #400 | none | no runs found | P1: targeted tests reported; DCO #399 and scope pending |
| [GS Quant #405](https://github.com/goldmansachs/gs-quant/pull/405) | focused extraction of #400 | none | no runs found | P1: targeted tests reported; DCO #399 and scope pending |
| [GS Quant #404](https://github.com/goldmansachs/gs-quant/pull/404) | focused extraction of #400 | none | no runs found | P1: targeted tests reported; DCO #399 and scope pending |
| [Altair #4180](https://github.com/vega/altair/pull/4180) | [#2796](https://github.com/vega/altair/issues/2796) (open, `Closes`) | none | Code checks, Docs, Tests: success | P1: maintainer review |
| [GS Quant #399](https://github.com/goldmansachs/gs-quant/pull/399) | contributor DCO/NOTICE prerequisite | none | no runs found | **P0 dependency**: await upstream acceptance before advancing #404–#408 |

## P0 execution and ownership

1. **Do not merge GS Quant #400 or switch #404–#408 to ready:** six overlapping draft PRs are documented. The maintainer must choose whether #400 is abandoned/closed or smaller PRs are accepted. The broad branch is not proven integration-safe.
2. **GS Quant #399:** the DCO is a repository policy gate, not a code/test bug. Only upstream maintainers can accept it. Confirm commit trailers and NOTICE against the accepted DCO before requesting code review.
3. **Xarray #11713:** exact-head documentation examples were reportedly verified locally, but the PR reports a separate benchmark-check failure and previously flaky PyDAP network dependency. Xarray [#11717](https://github.com/pydata/xarray/pull/11717) was explicitly closed because skipping on outage was contrary to maintainer direction; discussion belongs in [#11718](https://github.com/pydata/xarray/issues/11718). Do not rewrite tests just to color the CI green.
4. **Vega-Lite #9956:** fork CI needs maintainer workflow approval. This is not a reason for another empty commit or to remove the CI checks.
5. **AI policies:** SciPy prohibits autonomous AI-agent PR submission and AI-authored maintainer dialogue; Xarray requires the contributor's own words and understanding. Do not delegate upstream communication to an agent.

## Completed / not completed in this audit

- Completed: enumeration, head metadata inspection, review submissions, recorded review threads, Actions/status discovery, issue relationship verification, AI-disclosure keyword audit, and closed-PR lesson extraction.
- Not completed: independently executing every external project's full CI/test matrix, acquiring maintainer approval, merging any external code PR, or resolving the separate Benchmark failure for Xarray #11713. These must not be represented as done.

Companion: [Open-source contribution guide](OPEN_SOURCE_CONTRIBUTION_GUIDE.md).
