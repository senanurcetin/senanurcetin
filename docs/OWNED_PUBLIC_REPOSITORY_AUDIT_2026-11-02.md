# Owned public repository documentation audit — 2026-11-02

**Source:** authenticated GitHub account repository listing and current default-branch repository trees/README files, examined on 2 November 2026. **Purpose:** distinguish a professional, evidence-backed portfolio from upstream forks, coursework and private work. This inventory is not a production, security or code-quality certification.

## Actual scope

The account listing returned **122 repository records**. Exactly **16** were identified by account metadata as **public, non-fork, non-archived** at this checkpoint. The other 106 records cannot be counted as 106 original published software products: they include upstream forks, educational exercises, private work and possibly archived repositories. Visibility, fork flag and archived flag are classification metadata, not authorship proof.

Each of the 16 public non-fork repositories was inspected for a default-branch root README and Markdown-style **relative** README links. Paths were checked against that repository's nontruncated recursive Git tree; query fragments were removed before target lookup. Slash-prefixed web application routes and external URLs are outside this file-path audit. A valid relative target only proves that the path exists in Git, **not** that the content is scientifically correct, that the artifact can be executed, or that a deployment is healthy.

| Public non-fork repository | Relative README links checked | Missing file / directory targets | Review classification |
| --- | ---: | ---: | --- |
| [GitHub profile](https://github.com/senanurcetin/senanurcetin) | 11 | 0 | Portfolio publication and cross-project navigation |
| [NEXUS DevOps Intelligence](https://github.com/senanurcetin/nexus-devops-intelligence) | 60 | 0 | Read-only developer-tool MVP; release gates not equivalent to production |
| [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot) | 18 | 0 | Industrial RAG, SECOM and separate GitHub API auditor |
| [Vision2DCS](https://github.com/senanurcetin/Vision2DCS) | 21 | 0 | Synthetic, human-reviewed P&ID research demo |
| [Excel/CSV Reporting](https://github.com/senanurcetin/excel-csv-reporting-automation) | 8 | 0 | Synthetic data pilot, documented security and contribution boundaries |
| [Visual QC](https://github.com/senanurcetin/visual-qc-project) | 30 | 0 | NEU-CLS image classification and separate retrieval evaluation |
| [MS Capital Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting) | 34 | 0 | Time-series research; optimistic historical blend and lower leaderboard disclosed |
| [OT-Sentinel](https://github.com/senanurcetin/ot-sentinel) | 38 | 0 | BATADAL detector benchmark; synthetic live demo |
| [NEXUS Commerce](https://github.com/senanurcetin/nexus-commerce-intelligence) | 39 | 0 | Source-separated dbt, KPI/BI and historical Olist work |
| [Smart Factory](https://github.com/senanurcetin/smart-factory-app) | 48 | 0 | AI4I and C-MAPSS separate experiments; no plant deployment |
| [CASMI26 Research](https://github.com/senanurcetin/enveda-casmi26) | 25 | 0 | MS/MS retrieval and ranking, independent family-holdout with weak C3 transfer |
| [PlantLog](https://github.com/senanurcetin/PlantLog-MERN) | 20 | 0 | Read-only synthetic guest demo; backend limited to local use |
| [APTOS Retinopathy](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy) | 12 | 0 | Medical imaging research, shortcut and external validation limits |
| [ChemView](https://github.com/senanurcetin/ChemView) | 18 | 0 | Fictional reactor/mixer HMI, not physical safety control |
| [IEEE-CIS Fraud Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics) | 27 | 0 | Historical fraud data, tested modeling and dashboard |
| [Kaggle S6E10](https://github.com/senanurcetin/playground-s6e10) | 0 | 0 | Dated training/competition experiments, not a maintained product |
| **Total** | **409** | **0** | **Relative README file/directory links only** |

## Actual documentation changes in this batch

- [CASMI26](https://github.com/senanurcetin/enveda-casmi26) has been added to the [profile](../README.md), [reviewer guide](REVIEWER_GUIDE.md), [technical index](PROJECT_REVIEW_INDEX.md), [provenance catalog](PROJECT_CATALOG.md), [capability matrix](capability-matrix.md) and [profile evidence manifest](portfolio-manifest.json). The C2 fresh-family MRR@25 **0.8388** appears together with weaker unseen-candidate C3 **0.0373**. The historical public-examples overlap and lack of independent laboratory replication must remain visible; Kaggle logs and third-party base-model scores are not presented as private final results.
- The [metadata source of truth](../config/repository-metadata.json) now includes the CASMI26 research repository and its existing internal-study figure as an **image candidate**, not a Social Preview that was uploaded.
- Live GitHub About text was revised for Smart Factory, PlantLog, ChemView, CASMI26 and Kaggle S6E10 to avoid implying current factory control, external laboratory validation or a still-running competition. PlantLog's homepage was changed to the guest demo URL documented by its own README. No application source, hosting configuration or security settings were modified.

## Findings not to conceal

1. The **non-fork** GitHub flag is not a proof of sole authorship, and the presence of a README is not a code audit. The public [Football Intelligence team-project fork](https://github.com/senanurcetin/football-player-performance-analysis) and [GS Quant fork](https://github.com/senanurcetin/gs-quant) remain relevant professional evidence with explicit upstream attribution.
2. [CASMI26](https://github.com/senanurcetin/enveda-casmi26) and [Kaggle S6E10](https://github.com/senanurcetin/playground-s6e10) have no checked-in top-level `LICENSE` file at this checkpoint. **Do not infer an open-source grant from GitHub visibility** or add an arbitrary license without the owner's rights decision.
3. Local link checks do **not** validate external domains, notebooks, binaries, CI pass status, the public websites, GitHub Social Preview uploads, credential handling or the research conclusions. Recheck these separately when a release requires them.
4. The repository list includes additional forks/private educational histories not enumerated individually here to avoid presenting unverified work or private account details as a public product catalog.

## Maintenance rule

Keep a short, honest root README with a clear split between measured results, synthetic examples, code and production deployment. Update the [reviewer guide](REVIEWER_GUIDE.md), [catalog](PROJECT_CATALOG.md), [manifest](portfolio-manifest.json) and this inventory only when underlying research or GitHub repository state changes. Prefer accuracy over adding decorative badges, autogenerated screenshots or more workflows.
