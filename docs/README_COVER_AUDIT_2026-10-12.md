# GitHub README and cover presentation audit — 12 October 2026

> **Scope:** 16 public portfolio repositories in `docs/PROJECT_CATALOG.md`, plus the GitHub profile repository (17 metadata entries). VocabMaster is a separate product documentation stream.
>
> **Evidence:** current GitHub REST repository metadata, the first 80–110 README lines, and directory listings for the ten listed PNG screenshot candidates. This is a reproducible *presentation inventory*, not an assessment of model performance or deployed UI quality.

## Implementation log — README and evidence fixes merged

| Project | Merged PR | Completed source changes | Still requires hands-on verification |
| --- | --- | --- | --- |
| [Football Player Performance](https://github.com/senanurcetin/football-player-performance-analysis) | [#19](https://github.com/senanurcetin/football-player-performance-analysis/pull/19) | Historical six-image gallery labelled; 11-page PBIR / BigQuery-vs-synthetic scope clarified; overpay and underpricing interpretations qualified | Open/refresh 11 pages in Power BI Desktop; reconcile DAX and production SQL; take new genuine captures |
| [E-commerce Analytics](https://github.com/senanurcetin/E-commerce) | [#9](https://github.com/senanurcetin/E-commerce/pull/9) | Importable navy-blue Power BI JSON theme; three-page visual and semantic QA checklist; canonical case-study link | Obtain original PBIX/PBIP, import/inspect theme, reconcile current metrics, recapture historical screenshots; original violet editorial cover remains |
| [MSCapital Market Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting) | [#43](https://github.com/senanurcetin/ms-capital-market-forecasting/pull/43) | Source-rendered Streamlit screenshot provenance; v3 served versus v4 leaderboard model boundary; release/maintenance wording corrected | Review all seven live Streamlit pages, deployed commit and inference paths before refreshing screenshot or Social Preview |

**Interpretation:** these three PRs complete a first *README/source-presentation pass*, **not** full visual acceptance or all P0 backlog. The Football PBIR screenshot gate and Commerce Power BI Desktop gate remain on hold. MSCapital's screenshot remains a documented source-rendered historical capture, not verified live-server proof.

No GitHub Social Preview assets, repository About/Homepage settings, Power BI report binaries, numerical model results or production datasets were changed in this pass. Hosted CI was intentionally skipped while Actions minutes are exhausted.

## CI-independent implementation update — 13 October 2026

| Repository | Confirmed merged work | What the evidence proves | Not yet released/verified |
| --- | --- | --- | --- |
| [Visual QC](https://github.com/senanurcetin/visual-qc-project) | [#39](https://github.com/senanurcetin/visual-qc-project/pull/39) HMI styles/provenance and [#41](https://github.com/senanurcetin/visual-qc-project/pull/41) actual XLSX report | Workbook generator now produces a **formula-linked KPI Dashboard, Production Log and six-class Defect Analysis** sheet with two actual Excel charts; the HMI labels simulated production metrics | No new genuine deployed browser screenshot; Vercel READY production revision was behind repository main on inspection |
| [Smart Factory](https://github.com/senanurcetin/smart-factory-app) | [#8](https://github.com/senanurcetin/smart-factory-app/pull/8) real model-risk/OEE panels and [#11](https://github.com/senanurcetin/smart-factory-app/pull/11) reporting provenance | CSV response and README now explicitly describe the **shared worker-local simulation buffer** (last 240 readings), not a private visitor session or plant data | [#10](https://github.com/senanurcetin/smart-factory-app/pull/10) genuine browser capture and CircleCI workflow remains a separate unmerged proposal; public Render revision not independently verified |
| [Football](https://github.com/senanurcetin/football-player-performance-analysis) | [#22](https://github.com/senanurcetin/football-player-performance-analysis/pull/22) native 365-day PBIR visualization source changes | Four genuine data-bound chart definitions changed in both workspace and offline demo, without replacing reports with generated artwork | Full 11-page Power BI Desktop open/refresh, DAX check and re-capture not yet verified |

**Offline review performed in this update:** original XlsxWriter chart behavior was reproduced locally: hidden series columns need `show_hidden_data()` to avoid suppressing the pie-series data. The fix, source-linked formula tests and rejection-class validation are committed in Visual QC #41. Full project suites, CI and public deployment were **not** run or declared green for this offline review.

**Publication rule:** README screenshots and GitHub Social Previews must come from the **running, verified application/report** at a known code version, not generated concept panels. Do not substitute an Excel programmatic report for a Power BI Desktop screenshot.

## Second implementation pass — CI-free, 13 October 2026

| Repository | Merged implementation | Verification performed without CI | Remaining acceptance |
| --- | --- | --- | --- |
| [NEXUS web](https://github.com/senanurcetin/nexus-web-v2) | [#70](https://github.com/senanurcetin/nexus-web-v2/pull/70): previously scheduled or push-triggered hosted link-check/screenshot flows restricted to explicitly gated manual dispatch | Inspected all three affected GitHub workflow triggers and job gates | Live Vercel production SHA remained behind GitHub `main` during inspection; automated screenshot refresh is paused |
| [Smart Factory](https://github.com/senanurcetin/smart-factory-app) | [#14](https://github.com/senanurcetin/smart-factory-app/pull/14): real simulated, model-scored API readings now expose full ISO 8601 UTC timestamps in dashboard and CSV | Extracted embedded JavaScript and parsed it successfully; reviewed data/CSV tests and endpoint schema | Flask/Chromium runtime not re-executed; current Render release and genuine new screenshots unverified |
| [Visual QC](https://github.com/senanurcetin/visual-qc-project) | [#43](https://github.com/senanurcetin/visual-qc-project/pull/43): readable Availability/Performance/Quality chart labels and current API response/failure state in real HMI | Embedded HMI JavaScript parsed in V8, three-source-file diff and real source bindings inspected | Vercel production commit not refreshed; screenshot/interaction acceptance pending |
| [Football PBIR](https://github.com/senanurcetin/football-player-performance-analysis) | [#28](https://github.com/senanurcetin/football-player-performance-analysis/pull/28): eight more native Player Segmentation and Club/League chart source edits in both workspace and offline-demo | Verified all eight data-bound visual JSON documents and exact parity with production counterparts; Category/Y roles, chart type, typography and panel radius retained | Open, refresh and examine real Power BI Desktop report; no replacement screenshot available yet |

**Evidence boundary:** the changes above are real working application/report source files, **not** newly captured running dashboards. This pass did **not** invoke GitHub Actions or CircleCI. A parser/static inspection is not a replacement for live release, Power BI Desktop or end-to-end acceptance. Preserve existing historical screenshots until a verified capture from the intended deployed/source revision exists.

## Baseline findings

- **17 tracked entries after this change:** the original manifest omitted `GTM` although the project catalog and reviewer index included it. GTM is a **fork** and its default branch is **`master`**, not `main`.
- **10/10 previously listed PNG candidate paths exist** in the corresponding repository default branches. Existence and byte size alone do **not** prove the capture is current, authentic, accessible in a deployed product, or uploaded to GitHub's Social Preview setting.
- **7 entries have no approved Social Preview image candidate**: Excel/CSV Reporting, Olist, Greenweez, APTOS, Vision2DCS, GTM, and the GitHub profile. Several have conceptual SVG diagrams or external user-attachment screenshots in README; these are not automatically approved PNG social cards.
- **Metadata gaps:** Football's GitHub homepage is empty; Olist's public About description is less specific than the actual README; PlantLog's public homepage points to a generic `/#projects` anchor rather than its existing named case study route. The manifest now stages precise replacements for review. **No remote repository About or Social Preview settings were changed by this PR.**
- The public GitHub Topics field is populated on all 17 entries. The earlier four missing-topic priorities (MS Capital, Excel/CSV, Football, Olist) are no longer missing. Counts above the curated 5–8-topic guideline should be reviewed, **not** automatically overwritten.

## Screenshot-source verification

These are **existing GitHub files checked through directory metadata**; they are candidates for later manual visual review, not approved final cover designs.

| Repo | Existing image path | Uncompressed bytes |
| --- | --- | ---: |
| MS Capital | `docs/assets/mscapital-research-dashboard.png` | 97,227 |
| IEEE Fraud | `docs/assets/web_dashboard_executive_overview.png` | 175,819 |
| Smart Factory | `docs/assets/smart-factory-dashboard.png` | 235,336 |
| Visual QC | `docs/assets/visual-qc-dashboard.png` | 59,642 |
| Football | `docs/assets/screenshots/01_player_performance.png` | 230,183 |
| OT-Sentinel | `docs/assets/dashboard-normal.png` | 80,737 |
| E-commerce | `docs/assets/powerbi-channel-performance.png` | 347,816 |
| Ops-Copilot | `docs/assets/ops-copilot-case-study.png` | 988,865 |
| PlantLog | `docs/dashboard.png` | 71,518 |
| ChemView | `docs/assets/chemview-dashboard.png` | 144,801 |

Ops-Copilot's source PNG is close to 1 MB. This is not automatically a site image-budget violation: screenshot-source files and the portfolio's `public/og` output use different policies. Verify actual display quality and derivative share-card size rather than optimizing blindly.

## Repository presentation backlog

| Priority | Repositories | Next verification |
| --- | --- | --- |
| P0 | IEEE Fraud, MS Capital, Smart Factory, Visual QC | Compare README screenshots, app versions and portfolio case-study visuals; confirm every metric has experimental provenance |
| P0 | Football, E-commerce | Compare 11 Football report views (9 primary + 2 drill-through) and E-commerce Power BI screens with README captions; preserve source labels |
| P1 | Ops-Copilot, Vision2DCS, OT-Sentinel | Confirm actual interface captures, model/system boundaries and industrial safety disclaimers |
| P1 | APTOS, Greenweez, Excel/CSV Reporting | Decide whether a genuine capture exists; keep illustrations explicitly labelled conceptual |
| P2 | PlantLog, ChemView, GTM, Olist | Check archive/fork attribution, screenshot currency and missing share-card evidence |
| Cross-cutting | GitHub profile, nexus-web-v2 | Match featured project links, covers and labels to actual routes and repository proof |

## Staged metadata proposals (not applied remotely)

1. **Football:** point `homepage` to the existing `/projects/football-player-performance-analysis` route; About text explicitly mentions fork-based contributions.
2. **Olist:** replace generic public description with the existing detailed entry from `config/repository-metadata.json`, preserving upstream attribution.
3. **PlantLog:** point `homepage` to `/projects/plantlog-mern` rather than the homepage anchor.
4. **GTM:** now included in the manifest with its existing six Topics and `default_branch=master`; no synthetic demo or preview URL was added.

The sync tool defaults to **dry-run** and does not overwrite nonempty GitHub metadata. Review changes separately; narrow commands when an authorized GitHub CLI session is available:

```bash
python scripts/sync_repository_metadata.py
python scripts/sync_repository_metadata.py --repo football-player-performance-analysis --overwrite
python scripts/sync_repository_metadata.py --repo olist_database_analysis --overwrite
python scripts/sync_repository_metadata.py --repo PlantLog-MERN --overwrite

# After individual review, append --apply to the selected command.
```

## Preview and README acceptance criteria

- A real screenshot must be traced to a specific UI/repository revision; a diagram or editorial render must never be described as a live UI.
- All README-local images must resolve on the actual default branch; the candidate file must be inspected for legibility and sensitive information.
- Before preparing Social Preview outputs, final README cover sources and captions must be approved. Output cards should use the navy/blue portfolio palette and keep whole screenshots legible at GitHub crop sizes.
- Verify relevant live project links; do not imply an undeployed prototype or synthetic demo is production.
- Keep third-party dataset and upstream-fork attribution intact.
- Use local or deployment-time checks where possible. No new GitHub-hosted CI runs are required for this documentation audit.
- **GitHub Social Preview settings, About changes, pinned repositories and release publication remain unverified and incomplete until confirmed on GitHub.**

## Immediate follow-up

Review screenshots for the six P0 projects, resolve README-to-portfolio artwork mismatches, and only then regenerate final share-card proposals via `scripts/generate_social_previews.py` (dry-run first). Do not auto-publish the social cards as part of this inventory change.
