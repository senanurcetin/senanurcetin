# Repository storage audit (2026-10-12)

This inventory comes from GitHub's recursive Git tree metadata for the named repository default branches, not from a local filesystem guess. Sizes below are **uncompressed blob sizes**, not full Git history storage.

| Repository | Oversized tracked item(s) | Approximate file size | Handling decision |
| --- | --- | ---: | --- |
| [nexus-web-v2](https://github.com/senanurcetin/nexus-web-v2) (private) | `public/nexus-logo.png` | **5.91 MB** | Review transparent image size and lossless PNG/WebP optimization; keep the original until all usage paths work with a replacement |
| [E-commerce](https://github.com/senanurcetin/E-commerce) | `notebooks/olist-ecommerce-analysis.ipynb` | **18.57 MB** | Inspect code-cell outputs and embedded images, preserving code, markdown and experiment evidence; use the new notebook-audit helper before stripping anything |
| [olist_database_analysis](https://github.com/senanurcetin/olist_database_analysis) (fork) | `olist_geolocation_dataset.csv`, `olist.zip`, orders/items/reviews CSVs | **61.27 MB, 44.72 MB, 17.65 MB, 15.44 MB, 14.45 MB** respectively | Review licensing, provenance and the duplication between ZIP and extracted files before changing an educational/upstream fork |
| [football-player-performance-analysis](https://github.com/senanurcetin/football-player-performance-analysis) (fork) | Duplicate Power BI registered PNG resources under report and workspace folders | **4.72 MB** and **4.05 MB** per instance | Keep until Power BI Desktop/workspace integrity is checked; do not deduplicate files by name alone |
| [gs-quant](https://github.com/senanurcetin/gs-quant) (fork) | Generated `docs/_build` HTML and doctrees from upstream | **4.20 MB**, **2.32 MB**, etc. | Preserve fork/upstream expectations; do not rewrite upstream repository history solely to improve portfolio appearance |

## How to reduce storage without breaking projects

1. **Verify ownership and source rights.** A public Kaggle sample is not automatically licensed for redistribution. Do not delete or re-license upstream files without checking who maintains them and how they are used.
2. **Check references before altering assets.** Search application code, CSS, Power BI definitions, docs and build settings for the exact file path; run an authentic UI check after any image rename/format change.
3. **Preserve notebook code and evidence.** Examine the notebook's cell output types and whether plots are required for reviewer proof. Keep important published evidence in compact external images/reports. Remove transient outputs only after verifying the unchanged code/markdown.
4. **Use data download instructions for large external datasets.** Version small synthetic examples or deterministic transformation scripts instead of committing the entire original dataset twice. Store URLs and checksums when the original source allows that.
5. **Avoid history rewriting unless expressly approved.** `git rm` stops tracking a file in *future commits*; it does **not** remove that file from historic Git objects. Rewriting history changes commit identifiers and can break forks, links and collaborations. It is not authorized by this audit.
6. **Document the impact.** Note byte sizes before/after, image quality or model artifact parity, and reproducible steps. Changing project content can trigger GitHub Actions even when workflow files are untouched.

## Review priorities

- High-impact, comparatively low-risk: optimize **Nexus logo** as an alternate asset, switch references only after preview/testing.
- High-impact, moderate risk: strip **transient notebook outputs** in E-commerce, preserving all code and meaningful figures.
- High-impact, high-risk: dataset duplication in Olist and Power BI registered resources; require upstream/provenance and workspace verification first.
- Do **not** strip binary machine-learning model checkpoints without a documented reproducible replacement.

**Status:** The measured inventory and remediation guidance are recorded. Large tracked binaries are not deleted or rewritten by this document.
