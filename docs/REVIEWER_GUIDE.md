# Portfolio reviewer guide

**Audience:** hiring managers, technical interviewers, open-source maintainers, and potential collaborators. **Scope:** public repositories with inspectable code or dated evidence. Last curated: **2026-11-02**.

This is a navigation document, not a claim that every linked project is a production service or that all experiments can be rerun without externally licensed datasets. Start with the [GitHub profile](../README.md), then choose one evidence path below. The [full project index](PROJECT_REVIEW_INDEX.md) and [catalog with provenance labels](PROJECT_CATALOG.md) cover the wider collection.

## Quick decision paths

| Your focus | Start here | What to scrutinize |
| --- | --- | --- |
| Data Scientist / Risk ML | [Fraud Risk Intelligence](https://github.com/senanurcetin/ieee-fraud-detection-analytics) → [model validation evidence](https://github.com/senanurcetin/ieee-fraud-detection-analytics/blob/main/docs/model_validation_evidence.md) | Time-aware splits, repeated entities, class imbalance, calibration and review-queue costs |
| Time-series / Quant ML | [MS Capital Forecasting](https://github.com/senanurcetin/ms-capital-market-forecasting) → [validation protocol](https://github.com/senanurcetin/ms-capital-market-forecasting/blob/main/docs/VALIDATION.md) | Embargo, fold construction, blend-weight fitting, hold-out use and leaderboard mismatch |
| Computer vision / Reliability | [APTOS research](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy) → [scientific review](https://github.com/senanurcetin/APTOS-2019-diabetic-retinopathy/blob/main/docs/SCIENTIFIC_REVIEW.md) | Historical reused hold-out, metadata shortcuts, external-cohort transfer, clinical boundary |
| Scientific retrieval / molecular ML | [CASMI26 MS/MS research](https://github.com/senanurcetin/enveda-casmi26) → [fresh-family protocol](https://github.com/senanurcetin/enveda-casmi26/blob/main/docs/studies/fresh-training-family-holdout.md) | Candidate coverage vs ranking, sealed train/dev/test fitting, weak C3 transfer, external-source novelty gates and third-party competition-solution attribution |
| Analytics Engineering / BI | [Fraud warehouse lineage](https://github.com/senanurcetin/ieee-fraud-detection-analytics/blob/main/docs/bigquery_dbt_lineage.md) → [Commerce Intelligence](https://github.com/senanurcetin/nexus-commerce-intelligence) | SQL/dbt model contracts, KPI definitions and data provenance; commerce remains under development |
| Industrial AI | [OT-Sentinel](https://github.com/senanurcetin/ot-sentinel) → [case study](https://github.com/senanurcetin/ot-sentinel/blob/main/docs/case-study.md) | Detector measurements versus LLM explanation; public benchmark versus synthetic live telemetry |
| Developer Tools / LLM Apps | [Ops-Copilot](https://github.com/senanurcetin/Ops-Copilot) → [GitHub API integration](https://github.com/senanurcetin/Ops-Copilot/blob/main/docs/github-actions-integration.md) | Read-only API access, execution boundaries, tests and clearly disclosed incomplete functionality |

## Three ways to evaluate the work

**2-minute scan:** read the profile's selected-project table. Open a project README, check its purpose, stack, evidence type and limitation.

**10-minute technical review:** inspect the repository's methodology, test entry points and reproducibility instructions. Check what was run, the exact dataset/split, relevant baseline and whether a comparison is exploratory or held out.

**Deeper engineering review:** trace inputs and licensing, transformation contracts, model or application code, validation artifacts, CI history and deployment boundaries. A green badge or released tag establishes only the scoped checks for that revision, not independent operational adoption.

## Interpretation and provenance

- **Independent portfolio work** is distinct from **training exercises**, **contribution forks** and **collaborative educational work**. The [football analytics repository](https://github.com/senanurcetin/football-player-performance-analysis) is a documented Workintech team-project fork; do not attribute the shared upstream dbt foundation solely to this account.
- The [GS Quant risk work](https://github.com/senanurcetin/gs-quant) extends a fork of Goldman Sachs' library. The upstream package is not represented as original work.
- Fraud, market, medical, factory and OT results have different validation units and datasets. Scores across these projects are **not comparable rankings**.
- Finance work is research only, **not investment advice**. Retinopathy research is **not a medical device**. OT/DCS/HMI demos are **not certified industrial control or safety systems**.
- Demo interfaces may use public benchmarks or synthetic telemetry. A dashboard, hosted example or seeded simulation does not prove integration with a customer, industrial site or production dataset.
- A **work in progress** is intentionally not represented as a shipped, commercially ready product. Published timestamps and release records are the authoritative status markers.

## Open-source and technical collaboration

Read the [upstream contribution ledger](OPEN_SOURCE_ACTIVITY.md) for reviewed merges and open PRs; separate third-party acceptance from pull requests within self-owned repositories. The [contribution guide](OPEN_SOURCE_CONTRIBUTION_GUIDE.md) explains testing, attribution and evidence conventions.

For implementation-level feedback, open an issue in the relevant repository with a minimal reproduction, environment, expected/actual behavior and the file or model version. For private professional inquiries, use the contact route in the [profile](../README.md).

## Documentation maintenance rules

1. Put the **current** project promise, reproducible quickstart and limitations in the project's root README; keep dated experiments in deeper docs.
2. Label metrics with a dataset, split, baseline and evaluation date when available. Do not mix hold-out, cross-validation, public leaderboard and production monitoring.
3. Cross-check every case-study statement with code, tests, output artifacts or release records. Negative results are first-class evidence.
4. Prefer stable relative links inside a repository and stable public GitHub URLs between repositories. Do not link to private repository content as if it is publicly inspectable.
5. Update [portfolio manifest](portfolio-manifest.json) when projects or core claims change, and use the [site sync brief](site-sync-brief.md) before editing the portfolio website.

The [previous long-form profile](PROFILE_EVIDENCE_SNAPSHOT_2026-11-02.md) is preserved for historical reference only; do not treat it as a live status page.

For the **2026-11-02 portfolio-wide documentation inventory, executed changes, protected-branch PRs and verification gates**, see the [documentation execution record](DOCUMENTATION_EXECUTION_2026-11-02.md).
