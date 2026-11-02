# Repository presentation and release operations

This is a **checked, public-project maintenance guide** for the GitHub account. It does not claim that GitHub Topics, Social Preview settings, or new Releases have been published merely because a configuration file exists.

## 1. Metadata: apply only missing fields first

The [metadata manifest](../config/repository-metadata.json) now tracks 16 selected portfolio repositories plus the GitHub profile (17 entries), suggested Topics for gaps, and authentic screenshot candidates where available. The [synchronization script](../scripts/sync_repository_metadata.py) reads the current GitHub state, compares it to the manifest, and **defaults to dry-run**.

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

The [12 October README/cover audit](README_COVER_AUDIT_2026-10-12.md) is retained as historical context, **not** the latest inventory. On **2 November 2026** the metadata manifest was checked against repository trees, the stale E-commerce and Greenweez top-level entries were replaced by the consolidated [NEXUS Commerce Intelligence](https://github.com/senanurcetin/nexus-commerce-intelligence) entry, and broken Football / PlantLog image paths were repaired. Updated research/demo images are identified below. GTM still needs its `master` default-branch override. **Image path validity does not mean the account's actual Social Preview settings have changed.**

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

The redesigned generator uses the actual website palette (paper `#f7f8fa`, ink `#091625`, navy `#061524`, blue `#0572a8`), readable project-specific titles, and a **large uncropped source screenshot**. The earlier tiny screenshot + generic laptop placeholder style has been retired. It uses a light editorial design by default, and `--variant dark` offers a matching dark treatment. Neither style invents charts, metrics, or app interfaces. `--replace` is required to regenerate existing local images, and `--contact-sheet` writes a review grid for all previews.

The generator never fabricates screenshots; it leaves projects without verified images untouched. Verify each card visually, especially labels and cropped text, before using it publicly.

Upload the referenced **authentic PNG screenshot** through each repository's **Settings → General → Social preview** area. Use a centered visual and preview the resulting crop in GitHub before saving. A 1280 × 640 (2:1) canvas is a useful production target, but do not distort the screenshot or manufacture a dashboard or unverified score.

| Repository | Verified candidate in current repository | Evidence type |
| --- | --- | --- |
| MS Capital | [Research dashboard](https://github.com/senanurcetin/ms-capital-market-forecasting/blob/main/docs/assets/mscapital-research-dashboard.png) | Research interface |
| IEEE Fraud | [Executive dashboard](https://github.com/senanurcetin/ieee-fraud-detection-analytics/blob/main/docs/assets/web_dashboard_executive_overview.png) | Application interface |
| Smart Factory | [Factory dashboard](https://github.com/senanurcetin/smart-factory-app/blob/main/docs/assets/smart-factory-dashboard.png) | Simulated process dashboard |
| Visual QC | [QC dashboard](https://github.com/senanurcetin/visual-qc-project/blob/main/docs/assets/visual-qc-dashboard.png) | Simulated line interface |
| OT-Sentinel | [NEXUS normal-operation dashboard](https://github.com/senanurcetin/ot-sentinel/blob/main/docs/assets/nexus-dashboard-normal.png) | Synthetic OT telemetry |
| NEXUS Commerce | [Olist cohort analysis](https://github.com/senanurcetin/nexus-commerce-intelligence/blob/main/docs/advanced-analysis/cohort_retention.png) | Historical analytical figure, not UI |
| Football | [Power BI report gallery](https://github.com/senanurcetin/football-player-performance-analysis/blob/main/docs/assets/screenshots/NEXUS_Football_Page_Gallery.png) | Historical team-project BI screenshots |
| Ops-Copilot | [SECOM case study](https://github.com/senanurcetin/Ops-Copilot/blob/main/docs/assets/nexus-secom-case-study-desktop.png) | Public case-study screenshot |
| PlantLog | [Guest overview](https://github.com/senanurcetin/PlantLog-MERN/blob/main/docs/screenshots/nexus-demo-overview.png) | Synthetic guest demo |
| ChemView | [HMI dashboard](https://github.com/senanurcetin/ChemView/blob/main/docs/assets/chemview-dashboard.png) | Fictional mixing-vessel simulation |
| Vision2DCS | [P&ID research workspace](https://github.com/senanurcetin/Vision2DCS/blob/main/docs/assets/nexus-workspace-desktop.png) | Synthetic research/demo interface |
| APTOS | [Preprocessing stages](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy/blob/main/reports/figures/05_pipeline_stages.png) | Research figure, not clinical interface |

Excel/CSV Reporting Automation has no verified PNG/JPG screenshot candidate in this manifest. **No Social Preview images were uploaded or approved by this documentation update.** GitHub pin order likewise remains a separate profile UI setting; use [GitHub's documented Customize your pins control](https://docs.github.com/en/account-and-profile/how-tos/profile-customization/pinning-items-to-your-profile). Pinning cannot be changed through the GitHub GraphQL API described here.

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
