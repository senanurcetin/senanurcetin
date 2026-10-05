# 30-Second Project Summaries

## Fraud Risk Intelligence

An end-to-end fraud platform: DuckDB, BigQuery, and dbt feed a LightGBM ranker (ROC-AUC 0.9134) behind FastAPI and a live dashboard. The point is the review queue: threshold simulation shows the top 5% score band captures 58.32% of fraud labels.

## MSCapital Market Forecasting

A forecasting system over 804.5M rows with walk-forward validation and an embargo. The distinctive part is the investigation of why the graded score (0.128) sat below the internal estimate, reported openly.

## Visual QC Project

Steel-defect classification (macro F1 0.9392) with an entropy review queue that captures 81.8% of errors in the top 20%, plus an embedding-RAG assistant whose retriever and generator were chosen by measurement (94.8% hit@4, 75.7% of answer sentences grounded).

## Smart Factory App

Predictive-maintenance analytics on UCI AI4I (PR-AUC 0.9019, top-10% queue captures 94.1% of failures) plus a NASA C-MAPSS RUL case study with SHAP and drift detection, deployed live.

## APTOS-2019 Diabetic Retinopathy

A retinopathy grader that tests itself: shortcut baseline, pre-registered external validation (IDRiD AUC 0.984, Messidor-2 0.819), and an experiment showing the failure came from training labels. Served live, with limitations stated.

## E-commerce Analytics Portfolio

dbt Cloud, BigQuery, and Power BI turning raw events into 4 BI-ready marts, with 73 dbt tests, 30 DAX measures, and cohort/RFM analysis.
