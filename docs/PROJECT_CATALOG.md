# Project portfolio catalog

This catalog distinguishes **independent portfolio repositories** from **fork-based applied exercises**. It is a reading guide, not a claim that all projects are production deployments or that forked upstream code was authored here.

For evaluation details, follow each repository's README and linked methodology, validation or engineering evidence. Where a demo uses synthetic or public benchmark data, the corresponding case study should disclose that scope.

| Area | Repository | Provenance | Suggested review focus |
| --- | --- | --- | --- |
| Financial ML | [MS Capital Market Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting) | Independent | Walk-forward/embargo validation; hold-out vs. leaderboard results; research-only disclaimer |
| Fraud ML and analytics | [IEEE Fraud Detection Analytics](https://github.com/senanurcetin/ieee-fraud-detection-analytics) | Independent | Model validation, leakage protection, feature/warehouse lineage |
| Predictive maintenance | [Smart Factory](https://github.com/senanurcetin/smart-factory-app) | Independent | AI4I and C-MAPSS experiments, dashboard, model limitations |
| Computer vision / RAG | [Visual QC](https://github.com/senanurcetin/visual-qc-project) | Independent | Image classification evidence, review queue, RAG retrieval benchmarking |
| OT security | [OT-Sentinel](https://github.com/senanurcetin/ot-sentinel) | Independent | Rule/detector evidence, threat model, synthetic/demo vs benchmark conditions |
| Medical imaging ML | [APTOS-2019](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy) | Independent | Ordinal metrics, metadata-only baseline, external validation, non-clinical use |
| Web / marketing BI | [E-commerce](https://github.com/senanurcetin/nexus-commerce-intelligence) | Independent | dbt/DuckDB reproducibility, Power BI screenshots, session vs signup attribution |
| Finance and campaign BI | [Greenweez Analytics](https://github.com/senanurcetin/nexus-commerce-intelligence/tree/main/integrations/greenweez) | Independent | Finance margins, synthetic-seed controls, no unsupported campaign attribution |
| Analytics as a service | [Excel/CSV Reporting Automation](https://github.com/senanurcetin/excel-csv-reporting-automation) | Independent | Data-quality exceptions, reproducible synthetic pilot, [handoff criteria](https://github.com/senanurcetin/excel-csv-reporting-automation/blob/main/docs/PILOT_HANDOFF.md) |
| Industrial copilots | [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot) | Independent | RAG/operator information support vs certified safety decisions |
| Industrial visualization | [Vision2DCS](https://github.com/senanurcetin/Vision2DCS) | Independent | Visualization architecture and explicit non-production control boundaries |
| Industrial logbook | [PlantLog-MERN](https://github.com/senanurcetin/PlantLog-MERN) | Independent | API + React/MongoDB stack, development-only security assumptions |
| Industrial simulation | [ChemView](https://github.com/senanurcetin/ChemView) | Independent | Interlock simulation, HMI behaviors, no PLC/safety-rated deployment |
| Football analytics | [Football Player Performance](https://github.com/senanurcetin/football-player-performance-analysis) | Workintech training-team project; documented fork | Identify own analysis versus upstream contribution; temporal model validation |
| Web instrumentation | [GTM](https://github.com/senanurcetin/GTM) | Fork-based work | GA4 dataLayer test coverage and Jekyll storefront structure |
| SQL analysis | [Olist Database Analysis](https://github.com/senanurcetin/olist_database_analysis) | Fork-based work | PostgreSQL analysis, import portability and upstream attribution |

## Evaluation checklist for every featured project

1. **Ownership and provenance:** Mark upstream/fork work, third-party assets and contribution scope; keep source licenses and notices.
2. **Problem and decision:** Explain a real question, alternatives considered and why the chosen approach was used.
3. **Evidence:** Link executable checks, artifacts or screenshots. Label synthetic demos, CV folds, hold-outs, external benchmarks and live systems accurately.
4. **Failure modes:** Disclose leakage risks, negative findings, unavailable data, unsafe deployment boundaries and assumptions.
5. **Reproducibility:** Specify install/run commands, dependencies, dataset licenses, required secrets and computing constraints. Do not promise fully offline reproducibility when external data is required.
6. **Presentation:** Show a genuine demo/screenshot when available. Never use a generated conceptual image as proof of a working interface or validated score.
7. **Maintenance:** Keep release claims tied to actual tags, and avoid presenting inactive training exercises as maintained products.

## Repository hygiene policy

- **Feature vs training:** Feature a focused selection of independently developed projects on the profile and site; keep course forks available with clear attribution rather than inflating the independent project count.
- **Metadata:** For featured public repositories, maintain a concise About description, 5–8 relevant Topics, and an accurate homepage/demo link if one exists. GitHub Topics and Social Preview are repository settings and are not changed by this document.
- **Licenses:** Do not assign a new license to third-party or commercial code by default. Verify copyright ownership and upstream licensing first.
- **CI and hosting:** Status badges represent live external systems. A documentation update is not proof that CI, deployment, or the production service passed.
- **Security and privacy:** No real credentials, user records, protected datasets or client data in public branches, screenshots or demonstration artifacts.

This catalog focuses on the public projects available for reviewer inspection; private works are intentionally excluded.
