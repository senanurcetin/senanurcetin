# Capability Matrix

This matrix maps the main portfolio claims to specific public evidence. Each capability must be traceable to its source repository, evaluation protocol and documented limitations.

| Capability | Strongest evidence | Supporting evidence | Why it matters |
| --- | --- | --- | --- |
| Validation design | `ms-capital-market-forecasting` | `APTOS-2019-diabetic-retinopathy`, `ieee-fraud-detection-analytics` | Walk-forward with embargo, pre-registered external validation, and holdout risk-band reporting. |
| Analytics engineering | `ieee-fraud-detection-analytics` | `nexus-commerce-intelligence`, `nexus-commerce-intelligence/integrations/greenweez` | Tested dbt/BigQuery layers under the models. |
| Ranking and decision support | `ieee-fraud-detection-analytics` | `smart-factory-app`, `visual-qc-project` | Review-budget capture and threshold simulation instead of raw accuracy. |
| Scientific retrieval and candidate ranking | `enveda-casmi26` | `ieee-fraud-detection-analytics` | MS/MS retrieval plus LambdaRank; candidate-coverage oracle, sealed query-family evaluation and poor unseen-candidate C3 performance are reported together. |
| Computer vision | `visual-qc-project` | `APTOS-2019-diabetic-retinopathy` | Defect triage and medical imaging with confound checks. |
| LLM and RAG engineering | `visual-qc-project` | `Ops-Copilot`, `Vision2DCS` | Retrieval and faithfulness measured against baselines. |
| Predictive maintenance | `smart-factory-app` | `PlantLog-MERN` | Failure ranking and RUL regression tied to maintenance decisions. |
| BI delivery | `nexus-commerce-intelligence` | `ieee-fraud-detection-analytics` | Power BI, DAX, and statistical testing on governed marts. |
| Model serving | `APTOS-2019-diabetic-retinopathy` | `ms-capital-market-forecasting` | ONNX/FastAPI on a small host, Docker builds, CI on every push. |
| Industrial context | `ot-sentinel` | `ChemView`, `Vision2DCS` | Operator-facing and OT workflow breadth from prior automation work. |

## Lead case study roles

- `ieee-fraud-detection-analytics`: flagship for tested data plus modeling plus dashboard
- `ms-capital-market-forecasting`: validation discipline and honest reporting
- `visual-qc-project`: computer vision plus measured RAG
- `smart-factory-app`: predictive maintenance and ranked queues
- `APTOS-2019-diabetic-retinopathy`: external validation and stated limitations
- `nexus-commerce-intelligence`: analytics engineering and BI

## Supporting research and industrial demos

- `enveda-casmi26`: independent MS/MS research; internal family-holdout with explicit candidate-coverage and laboratory-generalization limits
- `Ops-Copilot`: developing industrial RAG and separately scoped GitHub REST tooling, not a certified operator service
- `ot-sentinel`: measured BATADAL detector research and **synthetic** operator telemetry, not live OT protection
- `Vision2DCS`: offline human-reviewed P&ID/HMI research; not a deployable DCS integration
- `ChemView`: fictional process and HMI simulation, no physical control
- `PlantLog-MERN`: synthetic guest demonstration with separately maintained local full stack

Do not use `archive-proof` to label current, independently maintained research without a dated reason. Forks and collaborative education projects must retain source attribution.
