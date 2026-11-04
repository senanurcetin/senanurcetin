# Senanur Çetin

**Data Scientist · AI Engineer · Analytics Engineering**  
*Industrial automation / DCS–SCADA background · Applied ML, data products and operator-facing systems*

I build analytics and machine-learning systems that can be **inspected, evaluated and reproduced within their stated constraints**: data contracts → modeling → validation → an interface for actual decisions. My industrial automation experience informs how I approach system boundaries, reliability and the gap between a research demo and an operational tool.

[**Portfolio & case studies**](https://senanur-cetin.vercel.app/) · [**Merged OSS case studies**](docs/OPEN_SOURCE_ENGINEERING_CASE_STUDIES.md) · [**Projects**](https://senanur-cetin.vercel.app/projects) · [**Technical review guide**](docs/REVIEWER_GUIDE.md) · [**Project evidence index**](docs/PROJECT_REVIEW_INDEX.md)

[LinkedIn](https://www.linkedin.com/in/senanur-cetin/) · [Kaggle](https://www.kaggle.com/senanuretin) · [Hugging Face](https://huggingface.co/senanurcetin) · [GitHub open-source activity](docs/OPEN_SOURCE_ACTIVITY.md) · [Email](mailto:senanur.cetin.work@gmail.com)

## Selected engineering work

Each result below belongs to a **particular experiment and evaluation design**. Links lead to public implementation and supporting evidence. Demos are not claims of customer deployment.

| Project | Engineering scope | Measured evidence and important limitation |
| --- | --- | --- |
| **[Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics)** | DuckDB → BigQuery/dbt → LightGBM → FastAPI/dashboard | 590,540 transactions; **ROC-AUC 0.9134**, average precision **0.5354**. Time-aware evaluation and identity/drift risks documented. [Model validation](https://github.com/senanurcetin/ieee-fraud-detection-analytics/blob/main/docs/model_validation_evidence.md) · [Demo](https://fraud-project-web.vercel.app) |
| **[MS Capital Market Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting)** | 804.5M raw rows; 292 engineered feature columns (264 distinct); walk-forward with embargo; ensemble ML | Historical five-fold ensemble cosine **+0.14088**, but submitted public leaderboard score **0.129**, below the field median. The historical blend fitted weights on scored folds; results are not nested-test estimates. [Validation limits](https://github.com/senanurcetin/ms-capital-market-forecasting/blob/main/docs/VALIDATION.md) |
| **[Visual QC](https://github.com/senanurcetin/visual-qc-project)** | Surface-defect vision, entropy review queue, evidence-grounded RAG | NEU-CLS macro F1 **0.9392**; top-20% review queue captures **81.8%** of observed errors. The RAG system is evaluated against keyword and no-retrieval controls. [Case study](https://github.com/senanurcetin/visual-qc-project/blob/main/docs/rag-case-study.md) |
| **[Smart Factory Analytics](https://github.com/senanurcetin/smart-factory-app)** | Predictive maintenance, separate remaining-useful-life analysis, SHAP and drift | AI4I benchmark PR-AUC **0.9019**; distinct NASA C-MAPSS RUL case study. **Not deployed to an industrial plant.** [Methods](https://github.com/senanurcetin/smart-factory-app/blob/main/docs/case-study.md) |
| **[APTOS Retinopathy Research](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy)** | EfficientNet-B0 grading, shortcut tests, examination-disjoint external validation | Historical ensemble QWK **0.9098** on an already reused hold-out; external-cohort performance varies substantially. **Research only; not a medical device.** [Scientific assessment](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy/blob/main/docs/SCIENTIFIC_REVIEW.md) |
| **[CASMI26 Molecular Identification](https://github.com/senanurcetin/enveda-casmi26)** | MS/MS candidate retrieval, molecular fingerprints, LambdaRank and group-separated evaluation | Fresh internal C2 MRR@25 **0.8388**, but the **C3 unseen-candidate setting drops to 0.0373**; no independent laboratory replication or final private competition result. [Study and limitations](https://github.com/senanurcetin/enveda-casmi26/blob/main/reports/advanced_review.md) |
| **[GS Quant Risk Analytics](https://github.com/senanurcetin/gs-quant)** | Risk dashboard, VaR / expected-shortfall and sequential backtesting | On a simulated regime shift, rolling 95% VaR had **63 breaches vs 37.5 expected**. Built **on a fork** of Goldman Sachs' library, with separate authored modules. [Repository](https://github.com/senanurcetin/gs-quant) |
| **[Football Intelligence](https://github.com/senanurcetin/football-player-performance-analysis)** | BigQuery, dbt, Power BI, valuation ML | **13 Power BI pages** (9 presentation, 2 drillthrough, 2 tooltip); post-cutover Desktop refresh not independently verified. A **Workintech team-project fork**: upstream work is explicitly credited, not presented as sole authorship. [Architecture & attribution](https://github.com/senanurcetin/football-player-performance-analysis/blob/main/docs/ARCHITECTURE.md) |

**More by discipline:** [Data science / model evaluation](docs/PROJECT_REVIEW_INDEX.md#data-science-and-model-evaluation) · [Analytics engineering & BI](docs/PROJECT_REVIEW_INDEX.md#analytics-engineering-reporting-and-data-products) · [Industrial AI](docs/PROJECT_REVIEW_INDEX.md#industrial-ai-and-operator-facing-interfaces).

## A closer look at the interfaces

**[Browse the 13-project visual gallery](docs/PROJECT_VISUAL_GALLERY.md)** — source-linked, portfolio-ready cover cards for analytics, ML and industrial research. Cards combine existing screenshots or research figures with editorial layout; they are **not** proof of a current deployment or completed GitHub Social Preview settings uploads.

These images are linked to the source repositories. The first two show application interfaces; the third is an **APTOS preprocessing research figure**, not a deployed clinical UI.

| Fraud risk dashboard | Smart factory dashboard | APTOS preprocessing research |
| :---: | :---: | :---: |
| [![Fraud analytics dashboard](https://raw.githubusercontent.com/senanurcetin/ieee-fraud-detection-analytics/main/docs/assets/web_dashboard_executive_overview.png)](https://github.com/senanurcetin/ieee-fraud-detection-analytics) | [![Smart factory maintenance dashboard](https://raw.githubusercontent.com/senanurcetin/smart-factory-app/main/docs/assets/smart-factory-dashboard.png)](https://github.com/senanurcetin/smart-factory-app) | [![APTOS image preprocessing experiment figure](https://raw.githubusercontent.com/senanurcetin/APTOS-2019-diabetic-retinopathy/main/reports/figures/05_pipeline_stages.png)](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy) |

**[Football Intelligence report gallery](https://github.com/senanurcetin/football-player-performance-analysis/tree/main/docs/assets/screenshots)** — Power BI screenshots from a collaborative training-team project, built from historical imported data rather than live sports feeds.

## Industrial AI and developer tooling

| Engineering project | What is demonstrable | Boundary |
| --- | --- | --- |
| [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot) | Industrial troubleshooting/RAG research and a **read-only GitHub Actions REST API auditor** with a local Node.js CLI, tests and CSV/JSON/Markdown exports. [API evidence](https://github.com/senanurcetin/Ops-Copilot/blob/main/docs/github-api-live-demo.md) | Independent, developing tooling; not an approved GitHub Developer Program product or official partnership |
| [OT-Sentinel](https://github.com/senanurcetin/ot-sentinel) | BATADAL anomaly-detector evaluation; max z-score **PR-AUC 0.427** versus chance **0.195** on the documented file | Demo telemetry is synthetic; the LLM explains detector outputs, not safety or control decisions |
| [Vision2DCS](https://github.com/senanurcetin/Vision2DCS) | Offline, human-reviewed P&ID/tag research. Tesseract's synthetic tag-only baseline **precision 0.5294 / recall 0.1915**. [Evidence matrix](https://github.com/senanurcetin/Vision2DCS/blob/main/docs/DEMO_EVIDENCE_MATRIX.md) | Not a certified PCS 7 / 800xA import, industrial controller or proven generalized OCR system |

**In development:** [NEXUS Commerce Intelligence](https://github.com/senanurcetin/nexus-commerce-intelligence) consolidates e-commerce analytics and BI work; its current repository is the source for progress. It is **not presented here as a completed commercial release**. Private assistant and website source repositories are intentionally excluded from public technical proof.

## Tooling and methods

| Area | Tools / methods used in linked work |
| --- | --- |
| **ML & evaluation** | Python, scikit-learn, LightGBM, XGBoost, PyTorch, SHAP, time-based hold-outs, embargo, GroupKFold, calibration, PR-AUC, QWK |
| **Data engineering & BI** | SQL, BigQuery, DuckDB, dbt, Pandas, Power BI / DAX, data-quality contracts and lineage |
| **AI applications** | RAG, LangChain, Gemini/Genkit, retrieval and answer-grounding evaluation, computer vision |
| **Application delivery** | FastAPI, Streamlit, React, Docker, local tests, GitHub Actions, deployment and release evidence |
| **Industrial background** | DCS/SCADA, Siemens PCS 7, ABB 800xA, commissioning and operator-focused systems |

## Contribution and evidence standards

I distinguish **my work**, **third-party upstream code**, **team contributions**, and **course exercises** rather than counting all visible repositories as original products. Third-party accepted contributions and open upstream PRs are tracked separately from maintenance of my own repositories.

- [Open-source contribution record](docs/OPEN_SOURCE_ACTIVITY.md) · [Contribution standards](docs/OPEN_SOURCE_CONTRIBUTION_GUIDE.md)

**Selected merged engineering case studies:** [xarray — scoped quantile warnings](docs/OPEN_SOURCE_ENGINEERING_CASE_STUDIES.md#1-xarray--all-nan-quantile-warning-isolation) · [pyjanitor — DataFrame memory isolation](docs/OPEN_SOURCE_ENGINEERING_CASE_STUDIES.md#2-pyjanitor--pivot_longer-outputinput-memory-isolation) · [pyjanitor — NumPy `.value` group optimization](docs/OPEN_SOURCE_ENGINEERING_CASE_STUDIES.md#3-pyjanitor--faster-homogeneous-numpy-value-groups). The linked work is merged upstream; test and performance limitations are documented.

- [Curated project catalog & ownership](docs/PROJECT_CATALOG.md) · [Reviewer guide](docs/REVIEWER_GUIDE.md)
- [Historical long-form profile with additional metrics, Kaggle snapshots and references](docs/PROFILE_EVIDENCE_SNAPSHOT_2026-11-02.md) — **dated archive, not a current status dashboard**

**My reporting rule:** measured results need their split, baseline, provenance and limitations. CI checks, hosted demos, or engineering prototypes alone do not establish clinical validity, industrial safety, production use, commercial adoption or professional-program acceptance.

**Professional contact:** [senanur.cetin.work@gmail.com](mailto:senanur.cetin.work@gmail.com) · [LinkedIn](https://www.linkedin.com/in/senanur-cetin/) · [Portfolio](https://senanur-cetin.vercel.app/).
