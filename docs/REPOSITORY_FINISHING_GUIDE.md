# Repository presentation and release operations

This is a **checked, public-project maintenance guide** for the GitHub account. It does not claim that GitHub Topics, Social Preview settings, or new Releases have been published merely because a configuration file exists.

## 1. Metadata: apply only missing fields first

The [metadata manifest](../config/repository-metadata.json) lists 16 featured repositories, suggested Topics for gaps, and authentic screenshot sources where available. The [synchronization script](../scripts/sync_repository_metadata.py) reads the current GitHub state, compares it to the manifest, and **defaults to dry-run**.

```bash
# From a local checkout of this profile repository:
gh auth login
python scripts/sync_repository_metadata.py
python scripts/sync_repository_metadata.py --apply

# After reviewing the difference, optionally improve an existing description:
python scripts/sync_repository_metadata.py --repo greenweez-finance-campaign-analytics --overwrite
python scripts/sync_repository_metadata.py --repo greenweez-finance-campaign-analytics --overwrite --apply
```

The first `--apply` run is designed to fill Topics that are currently empty, **not** replace already-present labels or descriptions. `--overwrite` is intentionally explicit and should only be used after examining the proposed changes. Avoid renaming, changing visibility, or setting fictional live demo links. The script makes no CI, Git tag or release changes.

The four initially empty-topic priorities—MS Capital, Excel/CSV Reporting, Football Player Performance (fork), and Olist Database Analysis (fork)—were checked on GitHub after the authenticated CLI run: all four now have Topics. Their present counts are 8, 7, 7, and 5 respectively. Existing nonempty Topics remain intact. Some About descriptions/homepage fields still need a separate human review; the default synchronization does not overwrite them.

## Current sequencing — Social Preview on hold

**As of 2026-10-12, the repository README artwork is being redesigned. Do not regenerate or upload new GitHub Social Previews yet.** The existing screenshot paths in the metadata manifest are only historical source candidates, not an approved current design. When the final README images are ready, update and verify the manifest, review every image source and caption, and only then generate/approve matching Social Preview cards. CI and repository README artwork are handled separately.

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

| Repository | Verified existing image path |
| --- | --- |
| MS Capital | [Research dashboard](https://github.com/senanurcetin/ms-capital-market-forecasting/blob/main/docs/assets/mscapital-research-dashboard.png) |
| IEEE Fraud | [Executive dashboard](https://github.com/senanurcetin/ieee-fraud-detection-analytics/blob/main/docs/assets/web_dashboard_executive_overview.png) |
| Smart Factory | [Factory dashboard](https://github.com/senanurcetin/smart-factory-app/blob/main/docs/assets/smart-factory-dashboard.png) |
| Visual QC | [QC dashboard](https://github.com/senanurcetin/visual-qc-project/blob/main/docs/assets/visual-qc-dashboard.png) |
| OT-Sentinel | [Normal-operation dashboard](https://github.com/senanurcetin/ot-sentinel/blob/main/docs/assets/dashboard-normal.png) |
| E-commerce | [Power BI dashboard](https://github.com/senanurcetin/E-commerce/blob/main/docs/assets/powerbi-channel-performance.png) |
| Football | [Player performance dashboard](https://github.com/senanurcetin/football-player-performance-analysis/blob/main/docs/assets/screenshots/01_player_performance.png) |
| Ops-Copilot | [Case study interface](https://github.com/senanurcetin/Ops-Copilot/blob/main/docs/assets/ops-copilot-case-study.png) |
| PlantLog | [Logbook dashboard](https://github.com/senanurcetin/PlantLog-MERN/blob/main/docs/dashboard.png) |
| ChemView | [HMI dashboard](https://github.com/senanurcetin/ChemView/blob/main/docs/assets/chemview-dashboard.png) |

For APTOS, a genuine interface image is available in the private website development context, but do not substitute a retinal diagnostic output for an evaluated clinical device. No verified direct PNG screenshot source was found in Excel/CSV, Greenweez, Vision2DCS or Olist; those settings need a real screenshot or a clearly marked **conceptual** graphic prepared separately. A verified source image is not itself proof the GitHub Social Preview setting has been updated.

## 3. Releases and versioning

**Already released (preserve):**

- MS Capital: `v1.1.0`.
- IEEE Fraud: `v1.0.9`.
- APTOS: `v1.0.0`.
- OT-Sentinel: `v0.3.0`.
- Smart Factory, Visual QC, Ops-Copilot: `portfolio-snapshot-2026-06` (historical snapshot tags; not semantic product versions).

**Candidates requiring review:** E-commerce Analytics and Excel/CSV Reporting Automation currently have no published GitHub Releases. Do not advertise `v1.0.0` until the code and output evidence at the proposed commit have been reviewed. Keep other prototype projects at `0.x` if breaking changes remain expected.

A release must include the tested revision, a short summary of what actually works, reproducibility instructions, known limitations, data rights, and the exact commit/tag. Use `gh release create` only after the tag's target commit and release notes have been reviewed.

A typical reviewed release command (example, **not run here**):

```bash
gh release create v1.0.0 --repo senanurcetin/REPOSITORY --target main --title "v1.0.0" --notes-file docs/RELEASE_NOTES_CANDIDATE.md
```

Never create historical fake dates, metrics, or production certifications. Updating project documentation by itself does not warrant a new release.

## 4. Storage and notebook hygiene

Review [the measured large-file inventory](REPOSITORY_STORAGE_AUDIT.md) before removing anything. Do not rewrite shared Git history or delete assets referenced by Power BI or existing builds without validating downstream dependencies. Forked datasets and upstream code need especially careful provenance checks.

## Completion boundary

The manifest, script, and these guides are **committed**. GitHub repository settings, Social Preview uploads and new Releases still require either an authorized repository administration tool or execution through an authenticated GitHub account. They are not marked complete until GitHub confirms the changes.
