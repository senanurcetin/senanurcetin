# Open-source contribution and maintainer activity

**Account:** [@senanurcetin](https://github.com/senanurcetin)  
**GitHub search snapshot:** 2026-10-26 (UTC)  
**Scope:** GitHub pull requests authored by this account in repositories **not owned by** `senanurcetin`. Counts are dated evidence, not live program eligibility or current CI results.

## Reproducible inventory

GitHub's pull-request search returned **50 third-party PRs**: **12 merged**, **30 open**, and **8 closed without merge** at the time checked. Repository ownership, not the fork's remote origin or an author's own fork, determines whether a PR is external. PRs in `senanurcetin/*` are excluded.

- [All 50 third-party PRs — live GitHub query](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+-user%3Asenanurcetin&type=pullrequests)
- [12 merged third-party PRs — live query](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Amerged+-user%3Asenanurcetin&type=pullrequests)
- [30 open third-party PRs — live query](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Aopen+-user%3Asenanurcetin&type=pullrequests)
- [Last-12-month merged-PR filter](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Amerged+merged%3A%3E%3D2025-10-26+-user%3Asenanurcetin&type=pullrequests)

GitHub search counts can change after this snapshot. Any support/funding application must check individual merges and rerun the live queries on the submission date; this document is **not** an eligibility certificate.

## Verified third-party merged pull requests

| Upstream | Merged PR | Contribution |
| --- | --- | --- |
| pyjanitor | [#1786](https://github.com/pyjanitor-devs/pyjanitor/pull/1786) | Include missingness in constant-column handling |
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

All 12 are in the 12-month window **2025-10-26 through 2026-10-26**, as returned by GitHub's filtered search. This is **not** 100 merged third-party PRs.

## Active upstream queue

**30 open third-party PRs** at snapshot time. Examples under independent upstream review include:

- [Anthropic Claude Agent SDK Python #1421](https://github.com/anthropics/claude-agent-sdk-python/pull/1421): transcript timestamp handling.
- [OpenAI Knowledge Retrieval #9](https://github.com/openai/openai-knowledge-retrieval/pull/9): citation-limit enforcement.
- [Vega Altair #4189](https://github.com/vega/altair/pull/4189): layering charts without local data.
- [Vega-Lite #9956](https://github.com/vega/vega-lite/pull/9956): CLI parsing/spec locale preservation.
- [Skrub #2347](https://github.com/skrub-data/skrub/pull/2347): missingness-indicator HOWTO.

An open PR is a proposed change, not an accepted or deployed upstream contribution. The [18 October upstream issue/review/CI audit](OPEN_SOURCE_PR_AUDIT_2026-10-18.md) remains a **historical** diagnostic, not the current PR inventory. Respect each upstream project's contribution and AI-assistance policy; do not automate maintainer conversation where it is prohibited.

## Owned-project maintenance (separate evidence)

Maintained public repositories include [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot), [NEXUS DevOps Intelligence](https://github.com/senanurcetin/nexus-devops-intelligence), [Vision2DCS](https://github.com/senanurcetin/Vision2DCS), [PlantLog-MERN](https://github.com/senanurcetin/PlantLog-MERN), and [Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics).

Their own pull requests, tests, releases, documentation and maintenance show work on **owned** repositories, but do **not** increase the external merged-PR count. Third-party usage, package downloads, downstream dependency reach and independent maintainers must be demonstrated separately. Do not interpret a green CI badge, star count, owner-authored PR, or a pre-production demo as proof of real-world ecosystem adoption.

## Verification limits and next checks

- The exact GitHub account **creation timestamp** has **not** been read from GitHub's `GET /users/senanurcetin` `created_at` field. It must be verified before any eligibility claim based on account age.
- Verify any program's **current official requirements**, geography, application form and terms immediately before applying.
- Evaluate adoption with actual traffic/install/dependent-package evidence. No externally verified installation count, package registry downloads or commercial customers are claimed here.
- Confirm author, upstream merge, license, and review status directly from the linked GitHub PR before quoting them.
- Never inflate counts by merging own PRs, generating artificial engagement, or treating `action_required` CI as a pass.

For practices and policy checks, see [the open-source contribution guide](OPEN_SOURCE_CONTRIBUTION_GUIDE.md). For separate project demonstrations and their limitations, see [the project catalog](PROJECT_CATALOG.md).
