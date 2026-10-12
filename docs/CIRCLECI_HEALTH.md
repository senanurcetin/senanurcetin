# Portfolio CircleCI health inventory

The authoritative project list is [config/circleci-projects.json](../config/circleci-projects.json).
It records **12 repositories** and their required CircleCI status-context names.
It does **not** claim that a config file proves CircleCI enrollment.

## Run without GitHub Actions minutes

From a checkout of the public profile repository:

```bash
python scripts/circleci_health.py
python scripts/circleci_health.py --format json
python scripts/circleci_health.py --strict
python -m unittest discover -s tests -p 'test_circleci_health.py' -v
```

The reporter uses read-only GitHub REST endpoints. For private VocabMaster and
NEXUS Web v2, set `GITHUB_TOKEN` in the local environment using
a token with **read-only repository access**. Do not paste credentials into an
issue, CI log, screenshot, or this repository. Projects that cannot be read
are shown as `UNAVAILABLE`; no successful check is invented.

## Status semantics

| Status | Interpretation |
|---|---|
| PASSED | All expected CircleCI commit-status contexts report success on the latest main SHA |
| PENDING | At least one expected CircleCI context is pending |
| FAILED | An expected CircleCI context reports failure or error |
| MISSING | One or more expected CircleCI context results are absent |
| SKIPPED | No CircleCI status and commit explicitly contains [skip ci] or [ci skip] |
| UNAVAILABLE | GitHub API could not be read; check token scope, network and rate limit |
| UNKNOWN | Reported status is not in an expected state |

A PASSED result means GitHub received successful CircleCI **statuses**.
It is not proof of a specific test's coverage, deployment success, verified
backup, correct production database connection, or successful external API.
VocabMaster deliberately fast-paths certain Markdown-only main commits:
its green docs-only status does not mean a new backend/frontend test run.
Inspect the job output and previous source-affecting commit.

Separate provider failures (such as Vercel build-rate-limit errors) are listed
under "Other failures", not treated as a failed CircleCI test. Do not replace
a missing CircleCI result with an old unrelated GitHub Actions check.

## Operational next steps

1. Check the latest SHA and exact CircleCI contexts, then read the linked job
   log for any failure or unexpectedly skipped job.
2. Verify that the intended repository is enrolled in CircleCI and its
   project uses `.circleci/config.yml` from `main`. The current last
   unconfirmed enrollment is MS Capital Market Forecasting.
3. Preserve existing backup, release, and production-health workflows until
   functionally equivalent replacements are independently proven.
4. Verify branch-protection rules separately. A passing CircleCI status does
   not automatically mean it is a *required* status check.
5. Re-run the inventory after an important main merge. It is a snapshot,
   not a continuously running monitoring service.

This command never triggers a pipeline, changes repository state, creates a
deployment, or consumes GitHub Actions runner minutes.
