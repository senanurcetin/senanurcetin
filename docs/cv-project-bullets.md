# CV Project Bullets

## Fraud Risk Intelligence

Headline:
Built an end-to-end fraud risk platform from raw transactions to a live executive dashboard.

- Modeled 590,540 transactions through a DuckDB, BigQuery, and dbt pipeline with 36 dbt models, 121 data tests, and 18 Python contract tests.
- Trained a LightGBM ranker (ROC-AUC 0.9134, average precision 0.5354) and reported risk-band quality on the holdout rather than only on the fitted split.
- Framed the model as a review queue with threshold simulation: the top 5% score band captures 58.32% of fraud labels at 40.13% precision.

## MSCapital Market Forecasting

Headline:
Built a walk-forward forecasting system over 804.5M rows and investigated why the leaderboard disagreed with the hold-out.

- Reduced 804.5M raw market-microstructure rows to 292 BigQuery features on a 16 GB laptop and validated with expanding walk-forward splits and a one-month embargo (+0.14088 cosine across five folds; +0.15171 on an untouched hold-out).
- Recorded a falsifiable forecast before submitting, tested six hypotheses for the gap to the graded 0.128 score, and reported the result even though it sits below the field median.
- Shipped a LightGBM/XGBoost/Ridge ensemble behind FastAPI, a seven-page Streamlit dashboard, and three CI jobs.

## Visual QC Project

Headline:
Built a steel-defect computer-vision case study with an entropy review queue and a measured RAG assistant.

- Classified 1,800 NEU-CLS images (accuracy 0.9389, macro F1 0.9392); the top-20% entropy queue captures 81.8% of errors.
- Benchmarked TF-IDF against embedding retrievers (BGE-base selected, 94.8% hit@4 vs 89.6%) and chose the generator and prompt by NLI-measured faithfulness (75.7% of answer sentences supported vs 20.7% without retrieval).
- Added a Flask/OpenCV inspection workflow with SQLite event logging and a live 3D digital twin deployed on Vercel.

## Smart Factory App

Headline:
Built predictive-maintenance analytics with ranked queues, SHAP, and drift monitoring.

- Benchmarked classifiers on UCI AI4I (ROC-AUC 0.9819, PR-AUC 0.8855, F1 0.8372); the top-10% queue captures 94.1% of failures at 9.4x lift.
- Added a NASA C-MAPSS remaining-useful-life regression case study with SHAP explanations and drift detection, and deployed a live risk-ranked maintenance queue.

## APTOS-2019 Diabetic Retinopathy

Headline:
Built a retinopathy grader that tests its own claims and reports where it fails.

- Trained an EfficientNet-B0 ordinal grader (five-fold QWK 0.8902) and showed a metadata-only baseline reaches QWK 0.652 without seeing a pixel.
- Pre-registered external validation: IDRiD referable AUC 0.984; Messidor-2 0.819, missing the pre-registered target, then traced the gap to training labels with a same-image control experiment.
- Served the ONNX ensemble live on a 512 MB host with 177 tests and a model card on Hugging Face. Not a medical device.

## E-commerce Analytics Portfolio

Headline:
Built a dbt, BigQuery, and Power BI pipeline that turns raw e-commerce events into BI-ready marts.

- Delivered 4 BI-ready marts with 73 dbt tests and 57 DuckDB CI tests, plus 50 documented DAX measures.
- Added cohort, RFM, and statistical-testing analyses for channel conversion.
