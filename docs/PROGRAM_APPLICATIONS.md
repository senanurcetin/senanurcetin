# Developer and open-source program applications

**Account:** [@senanurcetin](https://github.com/senanurcetin) · **Prepared:** 25 November 2026 (UTC)  
**Purpose:** one place for the evidence and ready-to-paste answers for six programs. The account owner submits every form; nothing here has been submitted.

**AI assistance:** this document was drafted with Claude Code (Anthropic). Every number below was re-checked live with `gh` and the pypistats.org API on the date above. The answers are drafts; the owner edits and approves them before pasting.

**Rule for every answer:** claims must match the evidence table. Weak fits are marked **Weak fit** and the answer says so instead of stretching the facts.

## Shared evidence (verified 25 November 2026)

| Claim | Value | How to re-check |
| --- | --- | --- |
| GitHub account age | Created **7 January 2026** (about 10.5 months) | `gh api users/senanurcetin --jq .created_at` |
| Merged PRs in repositories not owned by this account | **15** across 6 upstream owners: pyjanitor (3), Xarray (4), Altair (3), DuckDB docs (3), SciPy (1), Plotly.py (1) | [Live search](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Amerged+-user%3Asenanurcetin&type=pullrequests) · [ledger](OPEN_SOURCE_ACTIVITY.md) |
| Open external PRs | **10**: Claude Agent SDK Python [#1421](https://github.com/anthropics/claude-agent-sdk-python/pull/1421), [#1490](https://github.com/anthropics/claude-agent-sdk-python/pull/1490); Narwhals [#4094](https://github.com/narwhals-dev/narwhals/pull/4094); Altair [#4189](https://github.com/vega/altair/pull/4189); Xarray [#11843](https://github.com/pydata/xarray/pull/11843); plotnine [#1139](https://github.com/has2k1/plotnine/pull/1139); hvPlot [#1767](https://github.com/holoviz/hvplot/pull/1767), [#1768](https://github.com/holoviz/hvplot/pull/1768); pyjanitor [#1858](https://github.com/pyjanitor-devs/pyjanitor/pull/1858); sktime [#11538](https://github.com/sktime/sktime/pull/11538) | [Live search](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Aopen+-user%3Asenanurcetin&type=pullrequests) |
| External PRs closed without merge | **48** | [Live search](https://github.com/search?q=author%3Asenanurcetin+is%3Apr+is%3Aclosed+is%3Aunmerged+-user%3Asenanurcetin&type=pullrequests) |
| Review participation (not authorship) | Two review comments on Claude Agent SDK Python [#1493](https://github.com/anthropics/claude-agent-sdk-python/pull/1493), a PR **authored by another contributor** | [Comment 1](https://github.com/anthropics/claude-agent-sdk-python/pull/1493#issuecomment-6804687270) · [comment 2](https://github.com/anthropics/claude-agent-sdk-python/pull/1493#issuecomment-6808054378) |
| Maintained package | [`jsonl-utf8-guard`](https://pypi.org/project/jsonl-utf8-guard/) 0.3.0 on PyPI (MIT), source [offline-jsonl-workshop](https://github.com/senanurcetin/offline-jsonl-workshop) | `pip index versions jsonl-utf8-guard` |
| Package downloads | **367 in the last 30 days**, 229 in the last 7 days (pypistats, mirrors excluded). Early-stage; includes CI and bot traffic. | [pypistats](https://pypistats.org/packages/jsonl-utf8-guard) |
| Outside contributors | **2** people with merged PRs (4 PRs: [#42](https://github.com/senanurcetin/offline-jsonl-workshop/pull/42), [#44](https://github.com/senanurcetin/offline-jsonl-workshop/pull/44), [#51](https://github.com/senanurcetin/offline-jsonl-workshop/pull/51) by one contributor, [#50](https://github.com/senanurcetin/offline-jsonl-workshop/pull/50) by another), plus Dependabot | [Contributors](https://github.com/senanurcetin/offline-jsonl-workshop/graphs/contributors) |
| AI-assisted development record | Per-PR [AI assistance log](https://github.com/senanurcetin/offline-jsonl-workshop/blob/main/docs/AI_ASSISTANCE_LOG.md); reusable [claude-code-workflows](https://github.com/senanurcetin/claude-code-workflows) (MIT) | Repository files |
| GPU: RAPIDS | cuDF + XGBoost CUDA training **4.6–9× faster** than pandas + XGBoost CPU (16 threads) on 590,540 IEEE-CIS rows, RTX 3060 Laptop GPU; warm CSV parse about 3.5× faster; small data-prep steps are faster on CPU at this size | [ieee-fraud-detection-analytics](https://github.com/senanurcetin/ieee-fraud-detection-analytics#gpu-acceleration-with-rapids-november-2026) |
| GPU: TensorRT | ResNet-18 ONNX, **TensorRT FP16 3.286 ms/image** (batch 1), about 14× faster than CPU, same predicted class as CPU FP32 on all 1,800 NEU-CLS images; INT8 not covered | [visual-qc-project](https://github.com/senanurcetin/visual-qc-project#inference-acceleration-with-tensorrt) |
| License and recent activity | All repositories above: MIT; all pushed within the last 10 days | `gh api repos/senanurcetin/<repo> --jq .license.spdx_id,.pushed_at` |

**Corrections against earlier notes:** the package has **2** outside contributors with merges, not 3. Claude Agent SDK #1493 is **not** this account's PR (review comments only). Claude Agent SDK #1468 and OpenAI Knowledge Retrieval #9 are **closed**, not open.

## 1. GitHub Developer Program

- **Apply:** <https://docs.github.com/en/get-started/exploring-integrations/github-developer-program> (register link on that page)
- **Fit: Good.** The program is for people building on the GitHub API. This repository ships a [public-search PR auditor](../scripts/audit-external-prs.mjs) with [offline tests](../tests/audit-external-prs.test.mjs), and CI here validates documentation automatically.

**Ready-to-paste answers**

> **What are you building with the GitHub API?**  
> A dependency-free Node.js auditor that reads GitHub's public search API to produce a reproducible inventory of my external pull requests (merged, open, closed), with strict UTC date windows and checks for incomplete or duplicate records. It backs the evidence ledger in my profile repository and runs offline regression tests in GitHub Actions. I also use the `gh` CLI and Actions across my data/ML repositories for CI and release checks.

> **Website / repository:** https://github.com/senanurcetin/senanurcetin

## 2. GitHub Sponsors

- **Apply:** <https://github.com/sponsors/accounts> (Turkey is a supported region; payouts go through Stripe Connect)
- **Fit: Moderate.** Sponsors has no contribution threshold. The work worth funding is real but small: one package with 367 downloads a month and a steady upstream contribution record. Keep the tiers modest.

**Profile text (short bio)**

> Data scientist and AI engineer in Istanbul. I fix bugs and write documentation in the scientific Python stack (15 merged PRs to Xarray, pyjanitor, Altair, SciPy, DuckDB docs and Plotly.py) and maintain `jsonl-utf8-guard`, a dependency-free UTF-8 JSONL validator.

**Profile text (introduction)**

> I spend part of every week on open source: reproducing bugs in data libraries, sending tested fixes upstream, and maintaining a small validator for JSONL datasets used in ML pipelines.
>
> **What sponsorship pays for**
> - Time to keep upstream PRs moving through review (10 open right now in Xarray, Narwhals, Altair, hvPlot, plotnine, sktime and the Claude Agent SDK).
> - Maintenance of `jsonl-utf8-guard`: releases, issue triage and reviewing outside contributions.
> - GPU benchmarks I publish openly (RAPIDS cuDF, TensorRT), which run on my own hardware.
>
> I use AI coding assistants and log that use per PR, with test results, so reviewers can see what was checked.

**Suggested tiers:** $3 thanks · $10 name in the package README · $25 monthly progress note. No consulting or priority support tiers.

**`.github/FUNDING.yml`:** committed with the sponsor line commented out. Uncomment it only after the Sponsors profile is approved:

```yaml
# Uncomment after GitHub Sponsors approval:
# github: [senanurcetin]
```

## 3. NVIDIA Developer Program and NCA-ADS certification

- **Join (free):** <https://developer.nvidia.com/developer-program>
- **Certification:** NVIDIA-Certified Associate: Accelerated Data Science (NCA-ADS), $125, online proctored. Exam page: <https://www.nvidia.com/en-us/learn/certification/>
- **Fit: Good for the program, unproven for the exam.** The developer program has no entry bar. The two GPU projects show hands-on RAPIDS and TensorRT work, but the exam covers more of the RAPIDS stack than these projects use.

**Profile answers**

> **Area of interest:** Data science, GPU-accelerated ML (RAPIDS), inference optimization (TensorRT), RAG.  
> **What are you working on?** GPU versions of tabular and vision ML pipelines with published, reproducible benchmarks: RAPIDS cuDF + XGBoost CUDA on the IEEE-CIS fraud dataset (training 4.6–9× faster than CPU on an RTX 3060 Laptop GPU) and a TensorRT FP16 ResNet-18 for steel-defect inspection (3.3 ms/image). I also compare a hosted Nemotron model on NVIDIA NIM against local generators in a RAG case study.

**NCA-ADS study plan (four weeks, mapped to existing projects)**

Confirm the current exam blueprint on the certification page before starting; adjust topics to match it.

| Week | Topic | Already covered by | Gap to close |
| --- | --- | --- | --- |
| 1 | cuDF data loading, joins, group-bys; when GPU loses to CPU | IEEE-CIS RAPIDS benchmark (CSV read, identity join, encoding, group-by aggregates) | `cudf.pandas` zero-code-change mode; memory limits on a 6 GB GPU; Parquet vs CSV |
| 2 | GPU ML: XGBoost on CUDA, cuML | XGBoost CUDA training in the same benchmark | cuML (random forest, k-means, UMAP); rebuild one CPU baseline from the fraud pipeline in cuML |
| 3 | Scaling and graphs: Dask-cuDF, cuGraph | none | Small Dask-cuDF job over the full IEEE-CIS CSVs; one cuGraph example (PageRank on card/device links) |
| 4 | Inference, deployment and review | TensorRT FP16 benchmark; NIM in the RAG case study | INT8 calibration (currently not covered); Triton basics; two timed practice exams |

Book the exam only after week 4 practice scores are comfortable. Pay the $125 yourself through NVIDIA's site; check for Developer Program or DLI discounts first.

## 4. OpenAI Codex for Open Source

- **Apply:** <https://openai.com/form/codex-for-oss>
- **Fit: Weak fit.** The program asks for core maintainers or widely used projects. This account is an outside contributor upstream, and its own package is new (367 downloads a month, 2 outside contributors). Apply only if you want to be on record; expect a decline.

**Ready-to-paste answers**

> **Project:** jsonl-utf8-guard — https://github.com/senanurcetin/offline-jsonl-workshop (PyPI: jsonl-utf8-guard)  
> **Your role:** Creator and sole maintainer.  
> **Usage:** 367 PyPI downloads in the last 30 days (pypistats, mirrors excluded); two outside contributors with four merged PRs. It is an early-stage project, not yet widely used.  
> **Other open-source work:** 15 merged PRs as an outside contributor to Xarray, pyjanitor, Altair, SciPy, DuckDB docs and Plotly.py; 10 PRs under review.  
> **How would you use Codex?** Reviewing outside PRs against the validator's test suite, triaging bug reports into minimal reproductions, and preparing upstream fixes with red/green tests. I keep a per-PR AI assistance log so maintainers can see what was generated and what was verified.

## 5. Codex Open Source Fund

- **Apply:** <https://openai.com/form/codex-open-source-fund> (API credits, up to $25,000)
- **Fit: Weak fit.** The fund targets projects that use Codex or OpenAI models. No public repository here uses the OpenAI API, and the only OpenAI-related contribution ([openai-knowledge-retrieval #9](https://github.com/openai/openai-knowledge-retrieval/pull/9)) was closed without merge. Apply only with a concrete, small plan, and say plainly that it is a plan.

**Ready-to-paste answers**

> **Project:** jsonl-utf8-guard — https://github.com/senanurcetin/offline-jsonl-workshop  
> **Current OpenAI usage:** None in the project today. I use AI coding assistants (mainly Claude Code) and log their use per PR.  
> **Proposed use of credits:** Run Codex on incoming PRs and issues to draft reproductions and tests, and add an optional `--explain` mode that sends only the error location and schema (never record content) to an OpenAI model. Budget: under $1,000 for the first six months; I would report usage and results publicly in the repository.  
> **Why it matters:** JSONL is the default format for ML training and evaluation data; a validator that names the exact failing line and reason saves time in data pipelines.

## 6. Claude for Open Source (Ecosystem Impact track)

- **Terms and application:** <https://www.anthropic.com/claude-for-oss-terms>
- **Fit: Weak fit, with one hard blocker.** The terms ask for a GitHub account that is **at least two years old**; this one was created on 7 January 2026 (about 10.5 months). Check the current terms before applying; if the age rule still applies, wait until **7 January 2028**. The maintainer track (20+ outside contributors with merges, or 200k monthly downloads) is not met (2 contributors, 367 downloads). The Ecosystem Impact track is discretionary. License (MIT) and activity in the last 90 days are met.

**Ready-to-paste answers (for when eligible)**

> **Which track?** Ecosystem Impact.  
> **Contribution to the Claude ecosystem:** Two open PRs to the Claude Agent SDK for Python ([#1421](https://github.com/anthropics/claude-agent-sdk-python/pull/1421) naive transcript timestamps as UTC; [#1490](https://github.com/anthropics/claude-agent-sdk-python/pull/1490) sidechain flag consistency across session readers), and review comments on another contributor's PR ([#1493](https://github.com/anthropics/claude-agent-sdk-python/pull/1493)). [claude-code-workflows](https://github.com/senanurcetin/claude-code-workflows) (MIT) publishes a Claude Code skill for preparing upstream PRs with red/green tests, an AGENTS.md template and a per-PR AI assistance log template.  
> **Wider open-source work:** 15 merged PRs to scientific Python projects (Xarray, pyjanitor, Altair, SciPy, DuckDB docs, Plotly.py), and a small PyPI package built with Claude Code, with every AI-assisted change logged against its PR and CI result.  
> **Honest limits:** none of the SDK PRs has merged yet; the package is early (367 downloads a month, 2 outside contributors).

## Submission checklist (in order)

1. [ ] **NVIDIA Developer Program** — free, no bar. Join first; it may unlock DLI or exam discounts.
2. [ ] **GitHub Developer Program** — register with this repository as the integration.
3. [ ] **GitHub Sponsors** — set up Stripe Connect, paste the profile text, submit. After approval, uncomment `.github/FUNDING.yml` in a separate PR.
4. [ ] **NCA-ADS** — start the four-week plan; book the $125 exam only after practice tests.
5. [ ] **Codex for Open Source** — optional, weak fit; submit as-is or skip.
6. [ ] **Codex Open Source Fund** — optional, weak fit; only if you will build the proposed `--explain` plan.
7. [ ] **Claude for Open Source** — hold. Re-check the account-age rule; earliest date under the current wording is 7 January 2028. Re-run the evidence table first (an SDK merge would strengthen it).

Before each submission, re-run the live searches in the evidence table and update any number that changed.
