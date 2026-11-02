# Repository presentation and release operations

This is a **checked, public-project maintenance guide** for the GitHub account. It does not claim that GitHub Topics, Social Preview settings, or new Releases have been published merely because a configuration file exists.

## 1. Metadata: apply only missing fields first

The [metadata manifest](../config/repository-metadata.json) now tracks 17 selected portfolio repositories plus the GitHub profile (18 entries), suggested Topics for gaps, and authentic screenshot candidates where available. The [synchronization script](../scripts/sync_repository_metadata.py) reads the current GitHub state, compares it to the manifest, and **defaults to dry-run**.

```bash
# From a local checkout of this profile repository:
gh auth login
python scripts/sync_repository_metadata.py
python scripts/sync_repository_metadata.py --apply

# After reviewing the difference, optionally improve an existing description:
python scripts/sync_repository_metadata.py --repo nexus-commerce-intelligence --overwrite
python scripts/sync_repository_metadata.py --repo nexus-commerce-intelligence --overwrite --apply
```

The first `--apply` run is designed to fill Topics that are currently empty, **not** replace already-present labels or descriptions. `--overwrite` is intentionally explicit and should only be used after examining the proposed changes. Avoid renaming, changing visibility, or setting fictional live demo links. The script makes no CI, Git tag or release changes.

**2 November 2026 actual GitHub settings:** the professional About description was updated for the profile, Ops-Copilot, Vision2DCS, OT-Sentinel, Football Intelligence, NEXUS DevOps Intelligence, NEXUS Commerce Intelligence and Excel/CSV Reporting. Research-demo Topics replaced the misleading archive-proof Topic on Vision2DCS and OT-Sentinel; NEXUS DevOps Topics were populated. Football and Vision2DCS homepage links were corrected. Changes were applied through an authenticated GitHub CLI and checked against the public GitHub repository metadata. The manifest has been synchronized to avoid future overwrite drift.

## Current sequencing — Social Preview files verified, uploads pending

The [12 October README/cover audit](README_COVER_AUDIT_2026-10-12.md) is retained as historical context, **not** the latest inventory. On **2 November 2026** the metadata manifest was checked against repository trees, the stale E-commerce and Greenweez top-level entries were replaced by the consolidated [NEXUS Commerce Intelligence](https://github.com/senanurcetin/nexus-commerce-intelligence) entry, and broken Football / PlantLog image paths were repaired. Updated research/demo images are identified below. GTM's `master` default branch is already recorded in the metadata manifest and matches the live repository setting; no GTM branch override is pending. **Image path validity does not mean the account's actual Social Preview settings have changed.**

Create or approve preview artwork only after checking that it accurately represents the specific project (for example: APTOS image is a preprocessing research figure, and Vision2DCS uses synthetic P&ID examples). No screenshot should be labelled as a live customer or industrial deployment.

## 2. Social Preview: use real application evidence

GitHub Social Preview is a **repository setting**, not a README image. The available GitHub connector cannot upload it directly. Run:

```bash
python scripts/sync_repository_metadata.py --previews
```

To generate consistent **1280 × 640 PNG cards** using only the verified screenshots in the manifest, run locally:

```bash
python -m pip install Pillow
python scripts/generate_social_previews.py                       # dry-run
python scripts/generate_social_previews.py --write --replace --contact-sheet
# Optional dark variant, still in the website's navy/blue palette:
python scripts/generate_social_previews.py --variant dark --write --replace --contact-sheet
```

The redesigned generator uses the actual website palette (paper `#f7f8fa`, ink `#091625`, navy `#061524`, blue `#0572a8`), readable project-specific titles, and a **large uncropped source image (screenshot or research figure)**. The earlier tiny screenshot + generic laptop placeholder style has been retired. It uses a light editorial design by default, and `--variant dark` offers a matching dark treatment. Neither style invents charts, metrics, or app interfaces. `--replace` is required to regenerate existing local images, and `--contact-sheet` writes a review grid for all previews.

The generator never fabricates screenshots or research figures; it leaves projects without verified images untouched. Its project titles wrap within the text column and fail rather than allowing text to overlap source imagery; `Portfolio repository` avoids implying sole authorship from a non-fork flag. Verify each card visually, especially labels and image legibility, before using it publicly.

**2 November 2026 local preparation:** 13 real-source 1280 × 640 light PNG candidates and a contact sheet were generated in a local, untracked output folder and visually inspected. Two previously overflowing titles (APTOS and NEXUS Commerce) were corrected; research imagery now uses `SOURCE IMAGE` rather than claiming every graphic is a UI screenshot. Four entries without verified artwork were intentionally skipped. **These are local candidates only; no GitHub Social Preview settings were changed.**

Upload the **matching generated 1280 × 640 PNG card** for each repository through **Settings → General → Social preview**. Each card embeds its documented, authentic source screenshot or research figure; the raw source image and the generated card are different files. The local PNG cards are prepared under `C:\NEXUS-AI\incoming-projects\github-docs-social-previews-20261102`. Use a centered visual and preview the resulting crop in GitHub before saving. A 1280 × 640 (2:1) canvas is a useful production target, but do not distort the screenshot or manufacture a dashboard or unverified score.

| Repository | Verified source artwork | Evidence type | Published 1280 × 640 PNG card | GitHub upload page |
| --- | --- | --- | --- | --- |
| CASMI26 | [Internal ranking study](https://github.com/senanurcetin/enveda-casmi26/blob/main/docs/assets/advanced-internal-study.png) | Internal family-holdout figure, not external validation | [`enveda-casmi26.png`](../assets/social-previews/enveda-casmi26.png) | [Settings](https://github.com/senanurcetin/enveda-casmi26/settings) |
| MS Capital | [Research dashboard](https://github.com/senanurcetin/ms-capital-market-forecasting/blob/main/docs/assets/mscapital-research-dashboard.png) | Research interface | [`ms-capital-market-forecasting.png`](../assets/social-previews/ms-capital-market-forecasting.png) | [Settings](https://github.com/senanurcetin/ms-capital-market-forecasting/settings) |
| IEEE Fraud | [Executive dashboard](https://github.com/senanurcetin/ieee-fraud-detection-analytics/blob/main/docs/assets/web_dashboard_executive_overview.png) | Application interface | [`ieee-fraud-detection-analytics.png`](../assets/social-previews/ieee-fraud-detection-analytics.png) | [Settings](https://github.com/senanurcetin/ieee-fraud-detection-analytics/settings) |
| Smart Factory | [Factory dashboard](https://github.com/senanurcetin/smart-factory-app/blob/main/docs/assets/smart-factory-dashboard.png) | Simulated process dashboard | [`smart-factory-app.png`](../assets/social-previews/smart-factory-app.png) | [Settings](https://github.com/senanurcetin/smart-factory-app/settings) |
| Visual QC | [QC dashboard](https://github.com/senanurcetin/visual-qc-project/blob/main/docs/assets/visual-qc-dashboard.png) | Simulated line interface | [`visual-qc-project.png`](../assets/social-previews/visual-qc-project.png) | [Settings](https://github.com/senanurcetin/visual-qc-project/settings) |
| OT-Sentinel | [NEXUS normal-operation dashboard](https://github.com/senanurcetin/ot-sentinel/blob/main/docs/assets/nexus-dashboard-normal.png) | Synthetic OT telemetry | [`ot-sentinel.png`](../assets/social-previews/ot-sentinel.png) | [Settings](https://github.com/senanurcetin/ot-sentinel/settings) |
| NEXUS Commerce | [Olist cohort analysis](https://github.com/senanurcetin/nexus-commerce-intelligence/blob/main/docs/advanced-analysis/cohort_retention.png) | Historical analytical figure, not UI | [`nexus-commerce-intelligence.png`](../assets/social-previews/nexus-commerce-intelligence.png) | [Settings](https://github.com/senanurcetin/nexus-commerce-intelligence/settings) |
| Football | [Power BI report gallery](https://github.com/senanurcetin/football-player-performance-analysis/blob/main/docs/assets/screenshots/NEXUS_Football_Page_Gallery.png) | Historical team-project BI screenshots | [`football-player-performance-analysis.png`](../assets/social-previews/football-player-performance-analysis.png) | [Settings](https://github.com/senanurcetin/football-player-performance-analysis/settings) |
| Ops-Copilot | [SECOM case study](https://github.com/senanurcetin/Ops-Copilot/blob/main/docs/assets/nexus-secom-case-study-desktop.png) | Public case-study screenshot | [`Ops-Copilot.png`](../assets/social-previews/Ops-Copilot.png) | [Settings](https://github.com/senanurcetin/Ops-Copilot/settings) |
| PlantLog | [Guest overview](https://github.com/senanurcetin/PlantLog-MERN/blob/main/docs/screenshots/nexus-demo-overview.png) | Synthetic guest demo | [`PlantLog-MERN.png`](../assets/social-previews/PlantLog-MERN.png) | [Settings](https://github.com/senanurcetin/PlantLog-MERN/settings) |
| ChemView | [HMI dashboard](https://github.com/senanurcetin/ChemView/blob/main/docs/assets/chemview-dashboard.png) | Fictional mixing-vessel simulation | [`ChemView.png`](../assets/social-previews/ChemView.png) | [Settings](https://github.com/senanurcetin/ChemView/settings) |
| Vision2DCS | [P&ID research workspace](https://github.com/senanurcetin/Vision2DCS/blob/main/docs/assets/nexus-workspace-desktop.png) | Synthetic research/demo interface | [`Vision2DCS.png`](../assets/social-previews/Vision2DCS.png) | [Settings](https://github.com/senanurcetin/Vision2DCS/settings) |
| APTOS | [Preprocessing stages](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy/blob/main/reports/figures/05_pipeline_stages.png) | Research figure, not clinical interface | [`APTOS-2019-diabetic-retinopathy.png`](../assets/social-previews/APTOS-2019-diabetic-retinopathy.png) | [Settings](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy/settings) |

**Versioned artwork (2 November 2026):** The final 13 generated cards are now tracked in [`assets/social-previews/`](../assets/social-previews/), with a [13-card contact sheet](../assets/social-previews/contact-sheet.jpg). Each PNG links to its public, inspectable file in the table above. These copies make review, provenance and GitHub Settings uploads reproducible across devices; they are **not** evidence of actual Social Preview settings being updated.

**Upload verification:** for each project, inspect the GitHub-rendered preview after saving, then record the observed state as uploaded. Merely generating a file, adding a source screenshot, or opening the Settings page does not confirm a Social Preview upload. Keep the source-work attribution and research/synthetic labels visible. `contact-sheet.jpg` in the same local directory is an overview, **not** an upload candidate for an individual repository.

Excel/CSV Reporting Automation has no verified PNG/JPG screenshot candidate in this manifest. **No Social Preview images were uploaded or approved by this documentation update.** GitHub pin order likewise remains a separate profile UI setting; use [GitHub's documented Customize your pins control](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile). Pinning cannot be changed through the GitHub GraphQL API described here.

## 2a. Public link reachability — opt-in, not CI

The [bounded external-link audit](../scripts/audit_public_links.py) inspects external HTTPS links in the public profile and selected review documents, plus `repo_url`, `demo_url`, `release_url` and `homepage` fields in the portfolio/metadata manifests. It sends read-only HEAD requests with a bounded GET fallback, without account tokens or new workflows.

```bash
python scripts/audit_public_links.py
python scripts/audit_public_links.py --json
```

**2 November 2026 manual spot-check:** 57 distinct URLs were extracted from six public Markdown entry points; 54 answered HEAD `200`, LinkedIn and the Fraud demo refused HEAD (Fraud answered GET `200`), and the Kaggle profile `https://www.kaggle.com/senanuretin` returned GET `404` from the checker's network even though an older indexed page exists. The Kaggle result is **unresolved**, not proof of a deleted account: check it interactively before altering the identity link. A second scan of 32 unique manifest demo/repository URLs found 29 HEAD `200`, a Streamlit redirect (`303`), an APTOS Render timeout (not a confirmed outage), and a **confirmed `404`** for the old NEXUS Commerce homepage `/projects/e-commerce`. That homepage has been replaced in live GitHub metadata and the canonical manifest with the currently reachable `/projects/e-commerce-marketing-web-performance` target.

**Fresh tool verification (same day, after the homepage fix):** `python scripts/audit_public_links.py --timeout 5 --workers 6` checked **74 unique HTTPS URLs**, reporting **72 reachable**, one Streamlit `303` requiring redirect review, and one LinkedIn `999` access restriction. Kaggle and APTOS were reachable on this later pass. This demonstrates why a single failure, timeout or bot response should not automatically remove a portfolio link.

Network status is **not** operational acceptance. Login walls, rate limits, bot protection and sleeping Free-tier deployments may be inconclusive; do not automatically remove links or make CI fail on them. Any future result should be checked again in a normal browser or with an authenticated owner account before updating public documentation.

## 3. Releases and versioning

**Already released (preserve):**

- MS Capital: `v1.1.0`.
- IEEE Fraud: `v1.0.9`.
- APTOS: `v1.0.0`.
- OT-Sentinel: `v0.3.0`.
- Smart Factory, Visual QC, Ops-Copilot: `portfolio-snapshot-2026-06` (historical snapshot tags; not semantic product versions).

**Candidates requiring review:** NEXUS Commerce Intelligence and Excel/CSV Reporting Automation require independent release review before any new public version claim. Do not advertise `v1.0.0` until the code and output evidence at the proposed commit have been reviewed. Keep other prototype projects at `0.x` if breaking changes remain expected.

A release must include the tested revision, a short summary of what actually works, reproducibility instructions, known limitations, data rights, and the exact commit/tag. Use `gh release create` only after the tag's target commit and release notes have been reviewed.

A typical reviewed release command (example, **not run here**):

```bash
gh release create v1.0.0 --repo senanurcetin/REPOSITORY --target main --title "v1.0.0" --notes-file docs/RELEASE_NOTES_CANDIDATE.md
```

Never create historical fake dates, metrics, or production certifications. Updating project documentation by itself does not warrant a new release.

## 4. Storage and notebook hygiene

Review [the measured large-file inventory](REPOSITORY_STORAGE_AUDIT.md) before removing anything. Do not rewrite shared Git history or delete assets referenced by Power BI or existing builds without validating downstream dependencies. Forked datasets and upstream code need especially careful provenance checks.

## Completion boundary

The manifest and these guides are **committed**. The eight updated GitHub About descriptions, selected Topics, and two homepage fields were applied and verified separately through an authenticated CLI. **Social Preview uploads, pin rearrangement and any new Releases remain unperformed**; do not imply otherwise. None of these documentation changes proves a hosted release.
