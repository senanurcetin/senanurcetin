# Site Sync Brief

Use this file when the website implementation work starts. The goal is to keep the website fully aligned with the stronger GitHub portfolio surface without inventing new claims.

## Canonical content source

- Primary source: `docs/portfolio-manifest.json`
- Supporting source: `README.md`
- Deep-dive source: lead repo READMEs and case-study docs

## Homepage order

Default project order:

1. `Ops-Copilot`
2. `visual-qc-project`
3. `smart-factory-app`

Archive projects should appear later and visually subordinate.

## Hero positioning

Use this as the canonical headline direction:

`Industrial AI and applied data science engineer building practical software for factory teams, OT workflows, and operator-facing industrial systems.`

## What each lead project must show

### Ops-Copilot

- role: flagship case study
- core angle: document-grounded troubleshooting plus measurable failure-risk ranking
- required proof:
  - ROC-AUC `0.7659`
  - PR-AUC `0.1745`
  - `2.89x` lift at a `10%` review budget

### visual-qc-project

- role: support case study
- core angle: industrial computer vision plus QA workflow packaging
- required proof:
  - macro F1 `0.8093`
  - macro precision `0.8163`
  - `2.22x` review-yield lift vs random review

### smart-factory-app

- role: support case study
- core angle: predictive maintenance plus ranked maintenance queue logic
- required proof:
  - PR-AUC `0.8522`
  - F1 `0.8033`
  - top `10%` queue captures `92.6%` of holdout failures

## Required website link surfaces

Each lead project page should expose:

- repo link
- demo link
- release snapshot link
- short proof metrics
- one paragraph on what the repo proves

## Reading path defaults

The default recommended path should remain `Data + AI Roles`.

Other reading paths:

- `Industrial Systems Roles`
- `Product / Full-Stack Roles`

## Tone constraints

- Industrial-first, not generic SaaS
- Product-minded, but not over-marketed
- Conservative on claims
- No production-scale language unless the repo actually proves it
