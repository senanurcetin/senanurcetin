# Technical portfolio — reviewer index

An evidence-first map of selected **public** repositories. Start with the primary repository, then inspect datasets, model/data contracts, test evidence and limitations. This is a curated selection, **not** a claim that every repository is a standalone original project. Scores belong to the dated experiment and split stated in each repository.

## Data Science and model evaluation

| Project | Fast review | Core evidence / necessary caveat |
|---|---|---|
| [IEEE-CIS Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics) | [Engineering sources](https://github.com/senanurcetin/ieee-fraud-detection-analytics) | Time-based fraud ROC-AUC 0.9134; high random-split AUC can reflect repeated identities and drift |
| [MS Capital Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting) | [Engineering sources](https://github.com/senanurcetin/ms-capital-market-forecasting) | Walk-forward cosine +0.14088; shipped leaderboard +0.129, below public snapshot median |
| [APTOS Diabetic Retinopathy](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy) | [Engineering sources](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy) | Best five-fold ensemble test QWK 0.9098; metadata shortcut and external-domain loss exposed; not a medical device |
| [Smart Factory](https://github.com/senanurcetin/smart-factory-app) | [Engineering sources](https://github.com/senanurcetin/smart-factory-app) | Simulated AI4I risk evaluation plus a separate NASA RUL study; neither is plant-deployed |
| [Visual QC](https://github.com/senanurcetin/visual-qc-project) | [Engineering sources](https://github.com/senanurcetin/visual-qc-project) | NEU surface-defect classifier plus retrieval quality measurements; operator review remains necessary |
| [Football Player Analytics](https://github.com/senanurcetin/football-player-performance-analysis) | [Engineering sources](https://github.com/senanurcetin/football-player-performance-analysis) | Collaborative-project fork with attribution; high value-level R² compared against persistence baseline |

## Analytics engineering, reporting and data products

| Project | Fast review | Core evidence / necessary caveat |
|---|---|---|
| [E-commerce Analytics](https://github.com/senanurcetin/nexus-commerce-intelligence) | [Unified commerce evidence](https://github.com/senanurcetin/nexus-commerce-intelligence) | dbt marts and Power BI evidence; acquisition and session sources must not be conflated |
| [Greenweez Finance / Campaign](https://github.com/senanurcetin/nexus-commerce-intelligence/tree/main/integrations/greenweez) | [Integrated finance methodology](https://github.com/senanurcetin/nexus-commerce-intelligence/blob/main/integrations/greenweez/README.md) | dbt margin / advertising logic; portable DuckDB demo uses synthetic data |
| [Excel / CSV Reporting Pilot](https://github.com/senanurcetin/excel-csv-reporting-automation) | [Engineering sources](https://github.com/senanurcetin/excel-csv-reporting-automation) | Auditable issue quarantine, revenue reconciliation and static KPI pack; sample data is synthetic |
| [Olist Database Analysis](https://github.com/senanurcetin/olist_database_analysis) | [Engineering sources](https://github.com/senanurcetin/olist_database_analysis) | PostgreSQL schema and exploratory notebooks; not live company reporting |
| [GTM ToyStore](https://github.com/senanurcetin/GTM) | [Engineering sources](https://github.com/senanurcetin/GTM) | GA4-compatible event payload tests on an attributed Jekyll fork, not verified conversion uplift |

## Industrial AI and operator-facing interfaces

| Project | Fast review | Core evidence / necessary caveat |
|---|---|---|
| [OT-Sentinel](https://github.com/senanurcetin/ot-sentinel) | [Engineering sources](https://github.com/senanurcetin/ot-sentinel) | BATADAL detector evaluation, deterministic fallback; live telemetry is synthetic |
| [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot) | [Engineering sources](https://github.com/senanurcetin/Ops-Copilot) | Document-grounded troubleshooting and separate SECOM analysis; AI is not a safety authority |
| [Vision2DCS](https://github.com/senanurcetin/Vision2DCS) | [Engineering sources](https://github.com/senanurcetin/Vision2DCS) | Synthetic P&ID extraction cases and score code; exports are not vendor-certified |
| [ChemView](https://github.com/senanurcetin/ChemView) | [Engineering sources](https://github.com/senanurcetin/ChemView) | Server-side HMI interlock simulation; no PLC or certified safety system |
| [PlantLog](https://github.com/senanurcetin/PlantLog-MERN) | [Engineering sources](https://github.com/senanurcetin/PlantLog-MERN) | Asset registry and logbook full stack; local development configuration is not production-hardened |

## How to interpret the repository collection

The account also retains training exercises, coursework forks and open-source contribution forks. They are useful to show learning progress or attribution-backed contributions, **not** interchangeable with independently created and validated portfolio systems. Some client/prototype projects are private and intentionally omitted from this public index. The repository licence, original authorship and dataset terms remain project-specific.

For narrative role-based journeys and visual previews, see the [GitHub profile](../README.md) and the [project portfolio](https://senanur-cetin.vercel.app/projects).
