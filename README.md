# Senanur Cetin

**Data Analyst / BI · Data Scientist (risk and fraud) · AI / LLM Engineer.** I build evaluated machine-learning and analytics projects, from tested dbt and SQL pipelines to fraud-risk models and RAG applications, and publish every result with its evaluation scope and limitations, including the ones that fell short. Four years across industrial automation (DCS/SCADA) and applied data projects and training.

- Based in Istanbul, Turkey
- Portfolio: [senanur-cetin.vercel.app](https://senanur-cetin.vercel.app/)
- Project library: [senanur-cetin.vercel.app/projects](https://senanur-cetin.vercel.app/projects)
- Profiles: [LinkedIn](https://www.linkedin.com/in/senanur-cetin/) · [Kaggle](https://www.kaggle.com/senanuretin) · [Hugging Face](https://huggingface.co/senanurcetin) · [YouTube](https://www.youtube.com/@SenanurCetinn)
- Contact: [senanur.cetin.work@gmail.com](mailto:senanur.cetin.work@gmail.com)

## Current direction

- Three target tracks: Data Analyst / BI, Data Scientist (risk and fraud), and AI / LLM Engineer, in Istanbul or remote
- Workintech Data Pro Program completed from 1 March to 1 October 2026 across 24 sprints: Data Analyst Certificate (June 2026) and Data Scientist Certificate (September 2026)
- Industrial automation context across DCS/SCADA, validation, commissioning, and operator-facing systems

## Recruiter review paths

### Data Scientist

1. [Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics)
2. [MSCapital Market Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting)
3. [Visual QC Project](https://github.com/senanurcetin/visual-qc-project)
4. [Smart Factory App](https://github.com/senanurcetin/smart-factory-app)
5. [APTOS-2019 Diabetic Retinopathy](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy)

### AI Engineer

1. [Visual QC Project](https://github.com/senanurcetin/visual-qc-project): embedding-RAG assistant benchmarked against a keyword baseline and a no-retrieval control
2. [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot)
3. [Vision2DCS](https://github.com/senanurcetin/Vision2DCS)
4. [OT-Sentinel](https://github.com/senanurcetin/ot-sentinel)

### Analytics Engineering and BI

1. [Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics)
2. [E-commerce Analytics Portfolio](https://github.com/senanurcetin/E-commerce)
3. [Smart Factory Operations Analytics](https://github.com/senanurcetin/smart-factory-app)

## Verified project proof

| Project | Verified proof | Review surface |
| --- | --- | --- |
| [Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics) | 590,540 transactions, 38 dbt models, 126 data tests, 23 Python contract tests, 5 ML pipeline smoke tests, ROC-AUC `0.9134`, average precision `0.5354` | [Live dashboard](https://fraud-project-web.vercel.app) · [Case study](https://senanur-cetin.vercel.app/projects/fraud-risk-intelligence) |
| [MSCapital Market Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting) | 804.5M raw rows reduced to 292 BigQuery features; walk-forward validation with embargo: `+0.14088` cosine across 5 folds, `+0.15171` on untouched hold-out; shipped ensemble leaderboard score `0.129`, below the field median and reported as such; six-hypothesis investigation of the gap; FastAPI + Streamlit, 3 CI jobs. Research only, not investment advice | [Live dashboard](https://ms-capital-market-forecasting-mfy6rngulq4fpaovzrhntf.streamlit.app/) · [Case study](https://senanur-cetin.vercel.app/projects/mscapital-market-forecasting) |
| [Visual QC Project](https://github.com/senanurcetin/visual-qc-project) | 1,800 NEU-CLS images, accuracy `0.9389`, macro F1 `0.9392`, top-20% entropy queue captures `81.8%` of errors; RAG layer: exact source passage in top-4 for `94.8%` (TF-IDF `89.6%`), `75.7%` of answer sentences entailed by sources (no retrieval: `20.7%`) | [Case study](https://senanur-cetin.vercel.app/projects/visual-qc-project) · [Live demo](https://visual-qc-project-pearl.vercel.app) |
| [Smart Factory App](https://github.com/senanurcetin/smart-factory-app) | UCI AI4I predictive-maintenance case study plus a NASA C-MAPSS RUL-regression case study, SHAP, drift detection, DuckDB SQL; 10,000 AI4I records, ROC-AUC `0.9874`, PR-AUC `0.9019`, F1 `0.8293`, top-10% queue captures `94.1%` of failures at `9.4x` lift | [Case study](https://senanur-cetin.vercel.app/projects/smart-factory-app) · [Live app](https://smart-factory-app.onrender.com) |
| [APTOS-2019 Diabetic Retinopathy](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy) | 3,662 fundus photos, EfficientNet-B0 ordinal grader, 5-fold per-model mean QWK `0.8902`, ensemble test QWK `0.9091`; metadata-only shortcut baseline QWK `0.652`; pre-registered external validation: IDRiD referable AUC `0.984`, Messidor-2 `0.819` (below the pre-registered target, reported as is); 177 tests; not a medical device | [Live demo](https://aptos-2019-diabetic-retinopathy.onrender.com) · [Case study](https://senanur-cetin.vercel.app/projects/aptos-2019-diabetic-retinopathy) · [Model card](https://huggingface.co/senanurcetin/aptos-retinopathy-grader) |
| [E-commerce Analytics Portfolio](https://github.com/senanurcetin/E-commerce) | 4 BI-ready marts, 73 dbt tests, 57 DuckDB CI tests, 31 documented DAX measures, cohort/RFM and statistical testing | [Case study](https://senanur-cetin.vercel.app/projects/e-commerce-marketing-web-performance) |

## Working stack

- Machine learning and modeling: Python, scikit-learn, LightGBM, XGBoost, HistGradientBoosting, Random Forest, SHAP, PyTorch, imbalanced classification, computer vision (OpenCV, scikit-image)
- LLMs and AI engineering: Gemini API, Genkit, RAG, LangChain, multimodal prompting, TensorFlow/Keras
- Validation and measurement: time-based holdout, walk-forward with embargo, GroupKFold, calibration, threshold simulation, ROC-AUC, PR-AUC
- Analytics engineering and BI: SQL, BigQuery, dbt, DuckDB, Power BI, DAX, data modeling
- Analysis and experimentation: Pandas, NumPy, SciPy, EDA, cohort analysis, RFM, statistical testing
- Delivery: FastAPI, Flask, Streamlit, ONNX, Docker, MLflow, GitHub Actions, Render, Vercel
- Industrial context: DCS/SCADA, Siemens PCS7, ABB 800xA, VMware

## Other builds

- [nexus-agent](https://github.com/senanurcetin/nexus-agent): local-first personal AI agent with pooled free-tier LLM routing, Notion as database, queue-first automations, and an evaluation harness
- [VocabMaster](https://github.com/senanurcetin/VocabMaster): English vocabulary app with adaptive practice and word lists (beta) · [Live](https://vocab-master-olive.vercel.app)
- [nexus-web-v2](https://github.com/senanurcetin/nexus-web-v2): source of the [portfolio site](https://senanur-cetin.vercel.app/)

## Supporting and archive proof

- [Greenweez Finance & Campaign Analytics](https://github.com/senanurcetin/greenweez-finance-campaign-analytics): dbt and BigQuery finance/campaign reporting
- [GTM](https://github.com/senanurcetin/GTM): GTM and GA4-ready web analytics instrumentation
- [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot): industrial AI assistant for operator troubleshooting and document-grounded answers (archive)
- [OT-Sentinel](https://github.com/senanurcetin/ot-sentinel): OT monitoring and anomaly-workflow archive
- [Vision2DCS](https://github.com/senanurcetin/Vision2DCS): multimodal engineering workflow archive
- [ChemView](https://github.com/senanurcetin/ChemView): industrial HMI and telemetry UX archive
- [PlantLog-MERN](https://github.com/senanurcetin/PlantLog-MERN): industrial operations-software archive

## Verification standard

Public claims are tied to repository evidence, documented tests, current case-study pages, and verified industrial experience. Company projects and personal portfolio projects are presented as separate bodies of work.
