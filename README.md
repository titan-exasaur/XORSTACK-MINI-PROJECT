# Xorstack AI/ML Engineer – Mini Project & Assignments
**Submitted by:** Amith Kumar S

**Video Walkthrough:** [https://youtu.be/xJe5LQqcSgM](https://youtu.be/xJe5LQqcSgM)

**RAG Chatbot Repo:** [https://github.com/titan-exasaur/DOCUMENT-COPILOT-E2E](https://github.com/titan-exasaur/DOCUMENT-COPILOT-E2E)

---

## Mini Project – Shipment Anomaly Detection on Snowflake

**Problem:** Detect anomalies in shipment data to flag potential delays, losses, or irregular patterns.

**Approach:**

1. Created a free Snowflake trial account and set up a Warehouse, Database, and Schema to store the data.
2. Generated dummy shipment data using Mockaroo and uploaded it to Snowflake.
3. Performed feature engineering on the raw data to extract meaningful signals for anomaly detection.
4. Connected to the Snowflake database from the local environment using Snowflake credentials.
5. Trained a Machine Learning model for Shipment Anomaly Detection using the engineered features.
6. Stored model artifacts locally for future inference and reuse.

---

## Assignment I – Prompt Engineering: Invoice Data Extraction

**Task:** Write a prompt to extract structured data from an invoice and return the result in JSON format.

**Approach:**

The prompt is structured in four parts:

- **Role** – Tells the LLM what to act as (role-based prompting), setting the context for accurate extraction.
- **Condition** – Instructs the LLM to return output strictly in a fixed JSON schema format.
- **Rules** – A set of extraction rules the model must follow while mapping invoice fields to the schema.
- **Fixed Schema** – A predefined output structure that the model must always conform to, regardless of invoice layout variations.

This structure ensures consistency, handles edge cases (missing fields, ambiguous values), and produces reliable, parseable JSON output.

---

## Assignment II – Mini RAG Chatbot: PDF Q&A

**Repo:** [https://github.com/titan-exasaur/DOCUMENT-COPILOT-E2E](https://github.com/titan-exasaur/DOCUMENT-COPILOT-E2E)

An end-to-end RAG (Retrieval-Augmented Generation) chatbot that enables Q&A over PDF documents. Full implementation details, chunking strategy, embedding approach, and retrieval pipeline are documented in the linked repository.

---

## Assignment III – ML Project: CTR Prediction

**Dataset:** [Avazu CTR Prediction – Kaggle](https://www.kaggle.com/competitions/avazu-ctr-prediction/data)

**Steps followed:**

1. **Data Ingestion** – Loaded the Avazu dataset for processing.
2. **Exploratory Data Analysis (EDA)** – Analysed distributions, click rates, and feature patterns.
3. **Feature Classification, Engineering & Selection** – Identified and transformed categorical and numerical features relevant to CTR prediction.
4. **Model Selection & Training** – Selected and trained an appropriate model for binary classification (click / no-click).
5. **Model Evaluation** – Evaluated using standard metrics (AUC, accuracy, etc.).
6. **Code Modularization** – Structured the codebase into clean, reusable modules.
