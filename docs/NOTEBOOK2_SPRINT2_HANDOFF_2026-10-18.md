# Notebook 2 — Sprint 2 technical handoff (2026-10-18)

**Status:** Prepared for transfer; **not** represented as delivered to or executed by a separate notebook/agent. **Constraints:** no new upstream PRs, no maintainer/reviewer communications, no rewriting unrelated code, and no claims of CI success not backed by an exact SHA + run.

## Package NB2-S2-01 — Xarray #11713: CI provenance and regression isolation

- **Priority:** P0 diagnosis; no source modification currently justified.
- **Target:** [pydata/xarray#11713](https://github.com/pydata/xarray/pull/11713), exact head `d2765e37e2a9fc6ede38eff0d2ad6968fddb8387`.
- **Why:** `CI` run [38335579389](https://github.com/pydata/xarray/actions/runs/38335579389) has one failed `ubuntu-latest | test-py314 (flaky)` job [115094864746](https://github.com/pydata/xarray/actions/runs/38335579389/job/115094864746). The PR description identifies external PyDAP DAP2/DAP4 outages, but also reports a **different** Benchmark `Test Results` status failure, which cannot be treated as the `skipped` Benchmark workflow without independent evidence.
- **Acceptance gate 1:** Identify Benchmark `Test Results` check source, timestamp, exact target SHA, URL and whether it is a merge-required check; distinguish from a skipped `Benchmark` workflow. If details are not accessible, report UNKNOWN, not PASS.
- **Acceptance gate 2:** Reproduce 9 documented `Dataset.drop_duplicates` examples on the pinned head using the same source, capturing interpreter and dependency versions, before attributing any test failure to the docs patch.
- **Acceptance gate 3:** Compare changed-file scope (`xarray/core/dataset.py` docstring only) against failing job stack traces. Classify independently: external service, unrelated flaky, tool/check infrastructure, or change-caused.
- **Allowed implementation:** ONLY if change-caused regression is reproduced, prepare a minimal local tested patch on the existing fork branch; do not push without policy/owner approval. Do not revive skip-on-outage #11717.
- **Required evidence:** head SHA, exact test selection, exit status, artifacts/log links, regression/no-regression conclusion, `PASS/FAIL/NOT RUN/UNKNOWN` for each independent check.
- **Stop condition:** If the only failures are independent flaky jobs/third-party check artifacts, no code change; return diagnosis and correct blocking interpretation.

## Package NB2-S2-02 — GS Quant: DCO and overlapping draft quality gate

- **Priority:** P0 scope/integration gate and P1 targeted technical assurance; no unreviewed merge.
- **Targets:** [GS Quant #399](https://github.com/goldmansachs/gs-quant/pull/399) (DCO), [umbrella #400](https://github.com/goldmansachs/gs-quant/pull/400) and independent draft fixes [#404](https://github.com/goldmansachs/gs-quant/pull/404), [#405](https://github.com/goldmansachs/gs-quant/pull/405), [#406](https://github.com/goldmansachs/gs-quant/pull/406), [#407](https://github.com/goldmansachs/gs-quant/pull/407), [#408](https://github.com/goldmansachs/gs-quant/pull/408).
- **Pinned heads:** `#399 1302f7d61f7d60f6563c7ee4699fd58d5a7abb77`; `#400 39e3c57dd3d330d8cbc89335ac2d8ccc94be1f84`; `#404 2448229c90569bd630e76d05ed7e8464f222bdd3`; `#405 51aeda5e4d003dc92003b330e468665d866115f2`; `#406 dfd98508d0f6a01a898d28437a6158fd51985960`; `#407 be07818c8a86a65e6d9b11e02044355466a29de0`; `#408 bb2e9e3ecc74c14589d642d02c3f33befcaadefa`.
- **Known overlap:** `gs_quant/markets/report.py`, `gs_quant/risk/scenario_utils.py`, `gs_quant/mcp/tools/data/tools.py`, `gs_quant/timeseries/econometrics.py`, `gs_quant/session.py`. #400 is a 40-file draft; individual patches are not byte-for-byte duplicates. Confirm with current diffs before designing merge order.
- **Acceptance gate 1:** Inspect the upstream [CONTRIBUTING.md](https://github.com/goldmansachs/gs-quant/blob/master/CONTRIBUTING.md), status of #399, author attribution trailers and NOTICE; record which are blocking. DCO acceptance is maintainer-owned. Do not assume it is approved.
- **Acceptance gate 2:** Produce a per-file/hunk conflict matrix for #400 versus #404–#408 and distinguish shared logic, divergent behavior, test coverage and potential double application. Recompute if any SHA changed.
- **Acceptance gate 3:** Independently run the focused tests and Ruff on the exact PR heads when an executable environment is available. The PRs report 7, 9, 15, 37, 17 passes and #400 reports 91 targeted passes; they are *claims* until reproduced here and not proof of the full matrix.
- **Acceptance gate 4:** Suggest the smallest compatible integration sequence with rollback/stop criteria. Explicitly mark conditions requiring maintainer decision. Do not close #400, change draft state or create new upstream PR.
- **Allowed implementation:** Isolated local patch on an existing fork branch **only after** a concrete failed assertion or incompatible overlap is demonstrated; else produce conflict matrix plus test evidence, not churn.
- **Stop condition:** DCO or maintainer scope unresolved => leave PRs draft; mark BLOCKED / CLOSE CANDIDATE as applicable, with no merge claim.

## No third package

DuckDB #7494–#7496, Seaborn #4010–#4013, Vega-Lite #9956 and Plotly #5823 currently expose `action_required` upstream CI gates, not a verified source-level failure. Altair #4178/#4180 have green Actions evidence. Assigning Notebook 2 a speculative code rewrite would violate the quality-control constraint.

## Required return format

| Field | Required output |
|---|---|
| Repository / PR | Canonical URL + pinned/current SHA comparison |
| Root cause | Verified failure class, or UNKNOWN |
| CI/check evidence | Exact workflow/check URL, time, failure step |
| Test runs | Full command, environment, exit code and artifacts |
| Changes | Exact files/line locations, or `No code change justified` |
| Policy / ownership | Project rules, DCO/issue owner and maintainer gate |
| Recommendation | One next action and responsible party |
| Final status | `PASS`, `FAIL`, `BLOCKED`, or `UNKNOWN` with limits |

## Cross-notebook policy

Read [Sprint 2 audit](OPEN_SOURCE_SPRINT2_2026-10-18.md) and [open-source guide](OPEN_SOURCE_CONTRIBUTION_GUIDE.md). Any later update must re-fetch the live PR head before running checks. The requesting user must remain the human author of maintainer interaction wherever the host project's AI policy requires it.
