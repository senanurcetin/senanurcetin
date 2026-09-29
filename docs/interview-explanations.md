# Interview Explanations

## Fraud Risk Intelligence

Short explanation:

This is the project I lead with. It shows the whole path: tested dbt/BigQuery data, a LightGBM ranker, and a dashboard that treats the model as a review queue instead of a score.

What to emphasize:

- why average precision and review-budget capture matter more than accuracy on imbalanced fraud data
- why the holdout risk-band quality is reported next to the fitted split
- how dbt tests and Python contract tests keep the pipeline honest

## MSCapital Market Forecasting

Short explanation:

I wrote a forecast down before submitting, it was wrong (0.143 predicted, 0.128 graded), and I treated the gap as the research question. Six hypotheses were tested; one was confirmed and four falsified.

What to emphasize:

- why a random split would leak on overlapping 60-second windows and how the embargo fixes it
- that an internal gain below fold-to-fold noise is never a quantity that reaches a leaderboard
- that the score sits below the field median and the README says so

## Visual QC Project

Short explanation:

A real NEU-CLS defect benchmark, an entropy-based review queue, and a RAG assistant where every component was chosen by measurement.

What to emphasize:

- why the review queue is framed as capturing errors within a budget
- how NLI-measured faithfulness (75.7% vs 20.7% without retrieval) justified retrieval
- how the workflow and evaluation layers support each other

## Smart Factory App

Short explanation:

Predictive-maintenance analytics where the model output becomes a ranked maintenance queue, with a second case study on remaining useful life.

What to emphasize:

- why the failure target is imbalanced and why PR-AUC matters
- why a ranked queue is more realistic than treating every asset equally
- how SHAP and drift detection connect the model to maintenance decisions

## APTOS-2019 Diabetic Retinopathy

Short explanation:

A QWK of 0.90 does not say whether the model read the retina or the camera. I measured a metadata-only shortcut (0.652), pre-registered predictions for two external datasets, and reported the one that failed.

What to emphasize:

- the same-image control arm that isolated the failure to training labels
- what is not claimed: the deployed model is unchanged and the referral flag under-calls Moderate disease
- that it is not a medical device
