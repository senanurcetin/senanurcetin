# Open-source contribution guide

> Maintained from verified upstream reviews and pull requests. Last audited: 2026-10-18. This guide supplements, never overrides, the target repository's current policies.

## 1. Select and scope an issue

- Read the issue, linked PRs, contributor guide, PR template, AI policy, test instructions, and license before changing code.
- Confirm the issue is still open, the underlying behavior reproduces, and maintainers have not already chosen a different design.
- Prefer one problem, one minimal patch, and focused regression evidence per PR. For large AI-assisted changes, discuss the approach first when required.
- Reference the upstream issue precisely: `Closes owner/repo#123` for an actual fix; use `Related to` or `xref` for supporting changes. Do not close broad tracking issues accidentally.

## 2. Understand and validate every changed line

- Reproduce a bug or validate the exact documentation claim, then make a minimal targeted change.
- Test the **exact PR head**, record the commit SHA, commands, environment, PASS/FAIL/NOT RUN status, and any failure that remains.
- Do not treat a targeted test pass as proof that the complete matrix passed, or a skipped/action-required workflow as a failed test.
- Separate fork approval gates (`action_required`), flaky external services, genuinely failed tests, and missing runs. Never bypass branch protection or claim maintainer-run CI passed without evidence.
- A documentation example should actually be executed in the relevant runtime: notebook, browser, Python, SQL, or renderer. Check generated files and navigation links when the change requires them.

## 3. Review and communication

- Use the project's PR template, give a concise explanation of the defect, implementation, tests, limitations, and linked issue.
- Before responding to review comments, inspect the code and test results yourself. Address the specific feedback, then verify the new head.
- Do not automatically mark threads resolved as a substitute for the maintainer's decision; record resolved/unresolved status separately.
- Never send AI-written maintainer comments as your own when a repository prohibits this. The contributor must personally author the substance of any conversation.
- Do not repeatedly ping maintainers. If a review is pending, give them a reasonable interval; request attention only when justified by the repository's practice.

## 4. AI and authorship gate (repository-specific)

- **Pandas**: [contribution and AI policy](https://pandas.pydata.org/docs/dev/development/contributing.html) requires reporting specific automated tools, personally reviewing/editing generated results, no AI-authored maintainer dialogue, and an eligible issue assigned after `/take` **before** opening non-trivial PRs. `Closing Candidate`, `Needs Triage`, `Needs Discussion`, or `Needs Info` prevents assignment. Do not retry #71258 until #55848 is triaged and legitimately owned.
- **SciPy**: read [the official AI policy](https://scipy.github.io/devdocs/dev/conduct/ai_policy.html). The PR must disclose whether AI was used and, if used, name tools, uses, and AI-generated code or text. AI must not speak for you to maintainers (except translation/grammar editing), and autonomous AI-agent PR submission is not allowed. Be able to explain all code and licensing.
- **Xarray**: read [the official AI policy](https://docs.xarray.dev/en/stable/contribute/ai-policy.html) and [PR template](https://github.com/pydata/xarray/blob/main/.github/PULL_REQUEST_TEMPLATE.md). Fully review and understand every change. PR descriptions and review replies must express the human contributor's own reasoning; language polishing is acceptable, not AI-authored reasoning. Disclose and test AI-generated content.
- **GS Quant**: [CONTRIBUTING.md](https://github.com/goldmansachs/gs-quant/blob/master/CONTRIBUTING.md) requires the contributor DCO and NOTICE entry before the first code PR, plus the applicable `covered by:` commit trailer. Treat [DCO PR #399](https://github.com/goldmansachs/gs-quant/pull/399) as an outstanding dependency; do not mistake test success for DCO approval.
- **Altair, DuckDB, Seaborn, Vega-Lite, Plotly**: re-check each project's current contribution and PR instructions, and disclose AI assistance accurately where applicable. No uniform policy should be inferred merely because other projects use a disclosure section.
- Across all projects: no claims of manually reviewing, testing, understanding, or independently reproducing behavior unless the human has actually done so.

## 5. Lessons from closed upstream PRs

| Evidence | Transferable lesson |
| --- | --- |
| [SciPy #26391 — merged 2026-10-18](https://github.com/scipy/scipy/pull/26391) | Fill the complete PR template, include mandatory AI disclosure, obey RST spacing and section placement, and execute numerical examples rather than relying on prose alone. |
| [Xarray #11714 — merged](https://github.com/pydata/xarray/pull/11714) | Fix the behavior at the correct abstraction layer (`Variable.quantile`, not the generic dispatcher); use one focused regression and explicitly bound unsupported Dask behavior. |
| [Xarray #11715 — merged](https://github.com/pydata/xarray/pull/11715) | Prefer concise, general backend-safe warnings over unnecessarily narrow instructions; cover `open_dataset`, `open_mfdataset` and `load_dataset` appropriately. |
| [Altair #4179 — merged](https://github.com/vega/altair/pull/4179) | A successful documentation PR still needs end-to-end execution of the user-visible example; record what was and was not tested. |
| [Pandas #71258 — closed unmerged](https://github.com/pandas-dev/pandas/pull/71258) | Never open a pandas PR until the linked issue is eligible for `/take` and *actually assigned to you*. [#55848](https://github.com/pandas-dev/pandas/issues/55848) had `Closing Candidate`; the bot rejected `/take`, marked the PR `Needs Issue Assignment`, and the PR was closed. Preserve the patch but wait for maintainer triage, not a force-reopen. |
| [Xarray #11717 — closed unmerged](https://github.com/pydata/xarray/pull/11717) | Do not silence flaky external integration tests with opportunistic skips when maintainers want provider-independent fixtures; discuss replacement architecture via [#11718](https://github.com/pydata/xarray/issues/11718) first. |
| [GS Quant #398 — closed unmerged](https://github.com/goldmansachs/gs-quant/pull/398) | Keep the DCO prerequisite and its current accepted PR separate from code fixes; verify the actual upstream state before publishing another certificate PR. |

## 6. A reusable PR checklist

- [ ] An upstream issue or explicit scope agreement exists.
- [ ] Project-specific AI and contribution policies have been read **today**.
- [ ] I personally reviewed and can explain every change and example.
- [ ] The patch is minimal, license-compliant, and free of credentials or private data.
- [ ] Tests run against the exact head; commands, versions and limitations recorded.
- [ ] PR description follows the template and honestly discloses AI involvement.
- [ ] CI outcomes distinguish pass, fail, action-required, skipped and not-run.
- [ ] Review threads are addressed; maintainer-only gates remain marked pending.
- [ ] No duplicate or conflicting upstream PR was left unintentionally open.

## 7. Active queue

See [Sprint 2 recovery decisions (2026-10-18)](OPEN_SOURCE_SPRINT2_2026-10-18.md) for the 20 historically tracked PRs (19 OPEN + 1 MERGED), exact heads, CI/review gates and single-action ownership. Handoff work notes are not maintained as live instructions; re-check the linked upstream PRs and their current CI before acting. The [original audit](OPEN_SOURCE_PR_AUDIT_2026-10-18.md) remains as the baseline; revalidate before any merge or status statement.
