# Hi, I'm Senanur 👋

**Data Scientist · AI Engineer** — Istanbul · Open to Data Science and ML Engineering roles

I build machine-learning and analytics systems end to end: data pipelines and SQL models, validated ML, and the dashboards and APIs people use to make decisions. Before data science I worked in industrial automation (DCS/SCADA, Siemens PCS 7, ABB 800xA), which shapes how I think about reliability and the gap between a demo and a working tool.

[Portfolio](https://senanur-cetin.vercel.app/) · [LinkedIn](https://www.linkedin.com/in/senanur-cetin/) · [Kaggle](https://www.kaggle.com/senanuretin) · [Hugging Face](https://huggingface.co/senanurcetin) · [DEV](https://dev.to/senanurcetin) · [Email](mailto:senanur.cetin.work@gmail.com)

## Featured projects

| Project | What I built | Key result |
| --- | --- | --- |
| **[Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics)** | DuckDB → BigQuery/dbt → LightGBM → FastAPI dashboard | **ROC-AUC 0.913** on 590K transactions, time-aware split · [Demo](https://fraud-project-web.vercel.app) · RAPIDS cuDF + XGBoost CUDA: training [4.6–9× faster on GPU](https://github.com/senanurcetin/ieee-fraud-detection-analytics#gpu-acceleration-with-rapids-november-2026) |
| **[Visual QC](https://github.com/senanurcetin/visual-qc-project)** | Steel-defect classification, uncertainty-based review queue, grounded RAG | **Macro F1 0.939**; reviewing the top 20% catches **82%** of errors · TensorRT FP16: [3.3 ms per image](https://github.com/senanurcetin/visual-qc-project#inference-acceleration-with-tensorrt-november-2026), ~14× faster than CPU |
| **[Smart Factory Analytics](https://github.com/senanurcetin/smart-factory-app)** | Predictive maintenance and remaining-useful-life models with SHAP and drift checks | **PR-AUC 0.902** on AI4I |
| **[MS Capital Market Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting)** | Feature pipeline over 804M rows, walk-forward validation with embargo, LightGBM/XGBoost ensemble | 292 engineered features · FastAPI + Streamlit |
| **[APTOS Retinopathy](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy)** | EfficientNet-B0 grading with shortcut-learning and external-cohort audits | **QWK 0.910** on internal hold-out |
| **[OT-Sentinel](https://github.com/senanurcetin/ot-sentinel)** | Anomaly detection for water-network OT telemetry (BATADAL) | **PR-AUC 0.427** vs 0.195 chance |

<sub>These are research and portfolio projects, not production deployments. Each repository documents its data split, baseline and limitations.</sub>

| Fraud risk dashboard | Smart factory dashboard |
| :---: | :---: |
| [![Fraud analytics dashboard](https://raw.githubusercontent.com/senanurcetin/ieee-fraud-detection-analytics/main/docs/assets/web_dashboard_executive_overview.png)](https://github.com/senanurcetin/ieee-fraud-detection-analytics) | [![Smart factory maintenance dashboard](https://raw.githubusercontent.com/senanurcetin/smart-factory-app/main/docs/assets/smart-factory-dashboard.png)](https://github.com/senanurcetin/smart-factory-app) |

## Open source

**15 merged pull requests** in xarray, Vega-Altair, DuckDB docs, pyjanitor, plotly.py and SciPy. [Contribution record →](docs/OPEN_SOURCE_ACTIVITY.md)

**In review now:** [narwhals #4094](https://github.com/narwhals-dev/narwhals/pull/4094) (Python scalars from pandas rows, buffered `iter_rows`) · [Vega-Altair #4189](https://github.com/vega/altair/pull/4189) (layer scope model, proposed for the next major) · [xarray #11843](https://github.com/pydata/xarray/pull/11843) · [plotnine #1139](https://github.com/has2k1/plotnine/pull/1139) (slated for v0.16.0) · [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python/pulls?q=is%3Apr+author%3Asenanurcetin) ([live list](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Aopen+-user%3Asenanurcetin&type=pullrequests))

**PyPI:** [jsonl-utf8-guard](https://pypi.org/project/jsonl-utf8-guard/), a dependency-free, privacy-safe UTF-8 JSONL validator, published with Trusted Publishing from [offline-jsonl-workshop](https://github.com/senanurcetin/offline-jsonl-workshop). It has [three outside contributors](https://github.com/senanurcetin/offline-jsonl-workshop#contributors) so far; [v0.3.0](https://github.com/senanurcetin/offline-jsonl-workshop/releases/tag/v0.3.0) shipped work from two of them.

**Merged case studies:** [xarray — scoped quantile warnings](docs/OPEN_SOURCE_ENGINEERING_CASE_STUDIES.md#1-xarray--all-nan-quantile-warning-isolation) · [pyjanitor — DataFrame memory isolation](docs/OPEN_SOURCE_ENGINEERING_CASE_STUDIES.md#2-pyjanitor--pivot_longer-outputinput-memory-isolation) · [pyjanitor — NumPy `.value` group optimization](docs/OPEN_SOURCE_ENGINEERING_CASE_STUDIES.md#3-pyjanitor--faster-homogeneous-numpy-value-groups)

**Claude Code:** [claude-code-workflows](https://github.com/senanurcetin/claude-code-workflows) — a reusable skill and agent templates for evidence-based upstream PRs, plus PRs to the [Claude Agent SDK](https://github.com/anthropics/claude-agent-sdk-python/pulls?q=author%3Asenanurcetin) (under review).

## Get involved

New to open source, or looking for a small, well-scoped task? These repositories have issues labelled for first contributions, each with a reproduction and a clear definition of done:

- [offline-jsonl-workshop](https://github.com/senanurcetin/offline-jsonl-workshop/issues?q=is%3Aopen+label%3A%22good+first+issue%22%2C%22help+wanted%22) — a dependency-free Python JSONL validator. Questions are welcome in [Discussions](https://github.com/senanurcetin/offline-jsonl-workshop/discussions).
- [nexus-devops-intelligence](https://github.com/senanurcetin/nexus-devops-intelligence/issues?q=is%3Aopen+label%3A%22good+first+issue%22) — TypeScript tooling for reading GitHub Actions evidence.
- [claude-code-workflows](https://github.com/senanurcetin/claude-code-workflows/blob/main/CONTRIBUTING.md) — share a Claude Code skill or workflow you have used on real work.

I review every pull request. Please comment on an issue before starting so work isn't duplicated.

## Tech stack

- **ML:** Python, scikit-learn, LightGBM, XGBoost, PyTorch, SHAP, time-aware validation
- **Data & BI:** SQL, BigQuery, dbt, DuckDB, Pandas, Power BI / DAX
- **AI applications:** RAG, LangChain, Gemini, computer vision
- **GPU:** CUDA, TensorRT, ONNX Runtime, RAPIDS cuDF, XGBoost (CUDA)
- **Delivery:** FastAPI, Streamlit, React, Docker, GitHub Actions

## More

[All projects by discipline](docs/PROJECT_REVIEW_INDEX.md) · [Visual gallery](docs/PROJECT_VISUAL_GALLERY.md) · [Project catalog and ownership](docs/PROJECT_CATALOG.md) · [Reviewer guide](docs/REVIEWER_GUIDE.md)
