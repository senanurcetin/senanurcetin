# Open-source case studies

Three merged contributions to upstream Python data libraries. Each one links to the pull request and merge commit.

| Contribution | Problem | Approach |
| --- | --- | --- |
| [xarray #11714](https://github.com/pydata/xarray/pull/11714) | Expected all-NaN quantile warnings broke warnings-as-errors workflows | Narrowly scoped warning filter plus regression test |
| [pyjanitor #1820](https://github.com/pyjanitor-devs/pyjanitor/pull/1820) | `pivot_longer` output could share memory with the input DataFrame | Copy only when a flattened array may alias input storage |
| [pyjanitor #1822](https://github.com/pyjanitor-devs/pyjanitor/pull/1822) | Wide frames with many `.value` groups used slow repeated label selection | Positional NumPy fast path with a safe fallback |

## 1. xarray — all-NaN quantile warning isolation

**Upstream:** [pydata/xarray #11714](https://github.com/pydata/xarray/pull/11714) · [merged commit `3f29256`](https://github.com/pydata/xarray/commit/3f29256e912b9c63bf2b5ce0b91f163f5e3910f5) · merged 13 October 2026 · related [issue #9870](https://github.com/pydata/xarray/issues/9870)

**Problem.** NumPy's quantile fallback emits a `RuntimeWarning` for all-missing slices. Code that treats runtime warnings as errors stopped, even though `NaN` is the correct result.

**Change.** `Variable.quantile` now wraps the call in a local `warnings.catch_warnings()` and filters only the `All-NaN (slice|axis) encountered` message. Other warnings, the public API and computed values are unchanged. Release notes were updated.

**Test.** A two-column fixture (one all-missing column, one valid) runs with `RuntimeWarning` promoted to an error and `method="median_unbiased"`, and expects `[NaN, 2.0]` with no warning escaping.

**Review.** The first version filtered the warning more broadly. The reviewer asked for it at the specific call site instead, not inside the generic dispatcher. The revised patch was approved and merged. Dask per-block computations run outside this context and were left out of scope on purpose.

## 2. pyjanitor — `pivot_longer` output/input memory isolation

**Upstream:** [pyjanitor #1820](https://github.com/pyjanitor-devs/pyjanitor/pull/1820) · [merged commit `3d8d516`](https://github.com/pyjanitor-devs/pyjanitor/commit/3d8d5169ffed057e6fc6b9044348e454790816a8) · merged 26 October 2026 · fixes [issue #1770](https://github.com/pyjanitor-devs/pyjanitor/issues/1770)

**Problem.** Some flattening paths returned arrays that shared NumPy storage with the input. Mutating the `pivot_longer` output could silently change the caller's original data, including datetime values and index buffers.

**Change.** A `_ravel_values` helper copies a flattened array only when it may alias input storage. The related value-stacking and tiled-index paths got the same protection, without adding an unconditional DataFrame copy.

**Test.** Parameterized tests mutate output values and index columns across time-like arrays, sorting modes and several `.value` layouts, and check that the input is untouched. 24/24 buffer-isolation cases passed on Python 3.13, pandas 3.1 and NumPy 2.5, and all 7 upstream checks were green.

**Review.** Approved upstream. This fix was also the safety base for the `.value` optimization below.

## 3. pyjanitor — faster homogeneous NumPy `.value` groups

**Upstream:** [pyjanitor #1822](https://github.com/pyjanitor-devs/pyjanitor/pull/1822) · [merged commit `dd889d0`](https://github.com/pyjanitor-devs/pyjanitor/commit/dd889d084153394cb2335f1eafeeba3d3c3789e2) · merged 28 October 2026 · issue [#1821](https://github.com/pyjanitor-devs/pyjanitor/issues/1821)

**Problem.** Wide DataFrames with many `.value` groups needed repeated label-based column selection. A faster path had to keep dtype, null, ordering and aliasing behaviour identical.

**Change.** Builds one homogeneous NumPy value matrix and selects groups by position. Mixed dtypes and unsupported extension arrays use the existing path. Review rounds removed extra copies for fragmented frames and uneven groups. A separate benchmark script measures time and memory, with tracing kept out of the timing loops.

**Test.** 595 targeted tests passed (7 expected xfails), plus Ruff and a benchmark smoke run. Reviewers ran 7,200 and 10,080 differential cases on earlier revisions with no mismatches; their memory and performance findings led to further fixes before the merge.

**Benchmark.** Compared against the same branch with the fast path disabled. The gain depends on layout, fragmentation and dtype, so no single speedup number is quoted.

**Review.** Detailed code and memory reviews added regression tests and allocation improvements before final approval. Four files changed: production code, tests, benchmark and changelog.

## How I work on upstream changes

- Reproduce the edge case first, then keep the patch as small as the fix allows.
- Leave a regression test behind for each behaviour change.
- Treat maintainer review as part of the design; two of these three PRs changed shape because of it.
- AI tools helped with research, drafting and review; every change was checked and submitted by me.

See [Open-source activity](OPEN_SOURCE_ACTIVITY.md) for the full list, including PRs still under review.
