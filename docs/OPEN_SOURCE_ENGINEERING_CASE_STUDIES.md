# Selected merged open-source engineering case studies

**Scope:** three independently verifiable, *merged* contributions to upstream Python data libraries.  
**Evidence checked:** 4 November 2026. This is a curated selection, not an assertion that open pull requests have been accepted.

I approach open-source changes as engineering problems: reproduce the edge case, constrain the patch, test the accepted behavior, and account for maintainer feedback. Each study links directly to the upstream pull request and merge commit, which should be used as the source of truth.

| Accepted contribution | Problem addressed | Engineering emphasis |
| --- | --- | --- |
| [xarray #11714](https://github.com/pydata/xarray/pull/11714) | Expected all-NaN quantile warnings can interrupt warning-as-error workflows | Narrowly scoped warning handling and regression tests |
| [pyjanitor #1820](https://github.com/pyjanitor-devs/pyjanitor/pull/1820) | Reshaped output can alias input DataFrame buffers | Copy-on-alias protection and mutation isolation |
| [pyjanitor #1822](https://github.com/pyjanitor-devs/pyjanitor/pull/1822) | Repeated label-based selection of wide `.value` groups | Positional NumPy fast path, correctness and memory safeguards |

## 1. xarray — all-NaN quantile warning isolation

**Upstream:** [pydata/xarray #11714](https://github.com/pydata/xarray/pull/11714) · [merged commit `3f29256`](https://github.com/pydata/xarray/commit/3f29256e912b9c63bf2b5ce0b91f163f5e3910f5) · **merged 13 October 2026**  
**Related:** [issue #9870](https://github.com/pydata/xarray/issues/9870)

**The defect.** NumPy's quantile fallback can emit an expected `RuntimeWarning` for all-missing slices. Code that treats runtime warnings as errors may stop even though `NaN` is the correct result for that slice.

**The change.** Inside `Variable.quantile`, the accepted patch uses a local `warnings.catch_warnings()` context and filters only the `All-NaN (slice|axis) encountered` `RuntimeWarning` message. Unrelated warnings, the public API and computed values are unaffected. The final patch also updated the xarray release notes.

**Regression strategy.** A two-column fixture has one entirely missing column and one valid column. The test promotes `RuntimeWarning` to an exception, calls the quantile fallback with `method="median_unbiased"`, and checks for `[NaN, 2.0]` without an escaping warning. The patch spans three files.

**Maintainer feedback.** An initial broad approach was revised after a changes-requested review: warning suppression belongs at the specific call site, not inside the generic dispatcher. The revision was approved and merged. Dask's per-block computations execute outside this context and were deliberately excluded. The PR description reports external OPeNDAP service flakiness separately; it does not establish that a complete upstream test suite was rerun independently.

**What this demonstrates:** finding the right abstraction boundary, preserving observability and explicitly declaring non-goals.

## 2. pyjanitor — `pivot_longer` output/input memory isolation

**Upstream:** [pyjanitor #1820](https://github.com/pyjanitor-devs/pyjanitor/pull/1820) · [merged commit `3d8d516`](https://github.com/pyjanitor-devs/pyjanitor/commit/3d8d5169ffed057e6fc6b9044348e454790816a8) · **merged 26 October 2026**  
**Fixes:** [issue #1770](https://github.com/pyjanitor-devs/pyjanitor/issues/1770)

**The defect.** Some flattening paths could return arrays sharing NumPy storage with the input DataFrame. A mutation to `pivot_longer` output could then unexpectedly modify the caller's original data, including temporal values and index buffers.

**The change.** A selective `_ravel_values` helper copies a flattened array when it may alias input storage. Related value-stacking sites and tiled index handling were protected, without imposing an unconditional extra DataFrame copy. The design seeks both data isolation and appropriate allocation costs.

**Regression strategy.** Parameterized tests check mutations of output values and index columns, time-like arrays, sorting modes and multiple `.value` configurations. The PR records **7 successful upstream GitHub checks** and **24/24 independent representative buffer-isolation cases** on Python 3.13, pandas 3.1.0 and NumPy 2.5.4. The maintainer's larger fuzz matrix was **not independently rerun**, and local full-module execution was constrained by a missing `pandas_flavor` dependency.

**Maintainer feedback.** Reviewed and approved upstream. This correctness fix also created an essential safety foundation for the later `.value` performance optimization.

**What this demonstrates:** inspecting buffer ownership beyond simple equality tests and balancing correctness against allocation overhead.

## 3. pyjanitor — faster homogeneous NumPy `.value` groups

**Upstream:** [pyjanitor #1822](https://github.com/pyjanitor-devs/pyjanitor/pull/1822) · [merged commit `dd889d0`](https://github.com/pyjanitor-devs/pyjanitor/commit/dd889d084153394cb2335f1eafeeba3d3c3789e2) · **merged 28 October 2026**  
**Issue:** [#1821](https://github.com/pyjanitor-devs/pyjanitor/issues/1821)

**The bottleneck.** Wide DataFrames with many `.value` groups previously required repeated label-based column selection. A fast path had to avoid changing dtype, null, ordering and aliasing semantics.

**The change.** The accepted implementation constructs one homogeneous NumPy-backed value matrix and selects groups by positional indices. Mixed dtypes and unsupported extension arrays follow the existing fallback. Review iterations reduced unnecessary copies, including fragmented-frame and uneven-group cases. A separate benchmark script measures timing and memory without running tracing during timing loops.

**Regression strategy.** The final PR reports **595 targeted tests passed, 7 expected xfails**, plus Ruff and benchmark smoke checks in a specified local environment. Reviewers reported **7,200** and **10,080** differential test cases without result mismatches on *earlier* revisions and identified performance/memory problems that were subsequently addressed. Those reviewer runs **must not be reattributed** to the final merged commit.

**Measurement boundary.** The benchmark compared the final fast path to the *same branch* with the fast path disabled, not a separate current upstream `dev` checkout. No universal speedup percentage is claimed. Performance depends on layout, fragmentation and dtype.

**Maintainer feedback.** Detailed code and memory reviews led to additional regression tests and allocation improvements. A final approval preceded merge. Four files were changed, including production code, tests, benchmark and changelog.

**What this demonstrates:** optimization with controlled baselines, differential correctness testing, memory profiling and iterative maintainer collaboration.

## Engineering approach and attribution

- **Correctness first:** retain regression tests for warnings, buffer aliasing and output equivalence.
- **Evidence at the right revision:** distinguish tests on final heads, independent targeted runs and older-head reviewer probes.
- **Explicit limitations:** no inferred production adoption, global performance gain, or full-suite success beyond what an upstream run actually demonstrates.
- **Collaboration:** maintainers retain authority over design decisions, approvals and merges.
- **AI assistance disclosure:** AI-assisted tools supported research, drafting and review of these contributions and this portfolio text. Source-of-truth evidence is linked above; this document is not an independent certification of every environment or claim.

For the dated account-level contribution inventory (including *open* PRs), see [Open-source activity](OPEN_SOURCE_ACTIVITY.md). An open PR is proposed work, **not** a merged contribution.
