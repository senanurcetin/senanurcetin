# Capability Matrix

This matrix maps the main portfolio claims to specific public evidence. Use it when a recruiter or hiring manager wants to know which repository proves which capability.

| Capability | Strongest evidence | Supporting evidence | Why it matters |
| --- | --- | --- | --- |
| Validation design | `ms-capital-market-forecasting` | `APTOS-2019-diabetic-retinopathy`, `ieee-fraud-detection-analytics` | Walk-forward with embargo, pre-registered external validation, and holdout risk-band reporting. |
| Analytics engineering | `ieee-fraud-detection-analytics` | `E-commerce`, `greenweez-finance-campaign-analytics` | Tested dbt/BigQuery layers under the models. |
| Ranking and decision support | `ieee-fraud-detection-analytics` | `smart-factory-app`, `visual-qc-project` | Review-budget capture and threshold simulation instead of raw accuracy. |
| Computer vision | `visual-qc-project` | `APTOS-2019-diabetic-retinopathy` | Defect triage and medical imaging with confound checks. |
| LLM and RAG engineering | `visual-qc-project` | `Ops-Copilot`, `Vision2DCS` | Retrieval and faithfulness measured against baselines. |
| Predictive maintenance | `smart-factory-app` | `PlantLog-MERN` | Failure ranking and RUL regression tied to maintenance decisions. |
| BI delivery | `E-commerce` | `ieee-fraud-detection-analytics` | Power BI, DAX, and statistical testing on governed marts. |
| Model serving | `APTOS-2019-diabetic-retinopathy` | `ms-capital-market-forecasting` | ONNX/FastAPI on a small host, Docker builds, CI on every push. |
| Industrial context | `ot-sentinel` | `ChemView`, `Vision2DCS` | Operator-facing and OT workflow breadth from prior automation work. |

## Lead case study roles

- `ieee-fraud-detection-analytics`: flagship for tested data plus modeling plus dashboard
- `ms-capital-market-forecasting`: validation discipline and honest reporting
- `visual-qc-project`: computer vision plus measured RAG
- `smart-factory-app`: predictive maintenance and ranked queues
- `APTOS-2019-diabetic-retinopathy`: external validation and stated limitations
- `E-commerce`: analytics engineering and BI

## Archive proof roles

- `Ops-Copilot`: industrial AI assistant
- `ot-sentinel`: OT workflow and anomaly-response breadth
- `Vision2DCS`: multimodal engineering-tool thinking
- `ChemView`: industrial UX and HMI state modeling
- `PlantLog-MERN`: full-stack operations workflow design
