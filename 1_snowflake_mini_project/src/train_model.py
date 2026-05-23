# -------------------------------------------------------------------
# Importing Dependencies
# -------------------------------------------------------------------

import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from dotenv import load_dotenv
from snowflake.snowpark import Session
from imblearn.over_sampling import SMOTE

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


# -------------------------------------------------------------------
# Configuration
# -------------------------------------------------------------------

METRICS_FOLDER = "1_snowflake_mini_project/metrics"
ARTIFACTS_FOLDER = "1_snowflake_mini_project/artifacts"

os.makedirs(METRICS_FOLDER, exist_ok=True)

load_dotenv()

connection_parameters = {
    "account": os.getenv("SNOWFLAKE_ACCOUNT"),
    "user": os.getenv("SNOWFLAKE_USER"),
    "password": os.getenv("SNOWFLAKE_PASSWORD"),
    "role": os.getenv("SNOWFLAKE_ROLE"),
    "warehouse": os.getenv("SNOWFLAKE_WAREHOUSE"),
    "database": os.getenv("SNOWFLAKE_DATABASE"),
    "schema": os.getenv("SNOWFLAKE_SCHEMA"),
}


# -------------------------------------------------------------------
# Load data from Snowflake
# -------------------------------------------------------------------

session = Session.builder.configs(connection_parameters).create()
print("[INFO] Connected to Snowflake Successfully!")

query = """
SELECT
    shipment_mode,
    distance_km,
    package_weight,
    weather_condition,
    traffic_level,
    anomaly_flag
FROM SHIPMENT_RISK_VIEW
"""

df = session.sql(query).to_pandas()
print(f"[INFO] Rows fetched: {len(df)}")


# -------------------------------------------------------------------
# Preprocess data
# -------------------------------------------------------------------

categorical_cols = [
    "SHIPMENT_MODE",
    "WEATHER_CONDITION",
    "TRAFFIC_LEVEL",
]

for col in categorical_cols:
    encoder = LabelEncoder()
    df[col] = encoder.fit_transform(df[col])

X = df.drop("ANOMALY_FLAG", axis=1)
y = df["ANOMALY_FLAG"]


# -------------------------------------------------------------------
# Train-test split and SMOTE
# -------------------------------------------------------------------
# class a: 66, class b: 660
# class a: 660, class b: 660

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y,
)

smote = SMOTE(random_state=42)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

print("\n[INFO] After SMOTE balancing:")
print(y_train_smote.value_counts())


# -------------------------------------------------------------------
# Train model
# -------------------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=200,
    max_depth=8,
    random_state=42,
)

model.fit(X_train_smote, y_train_smote)

import joblib
joblib.dump(model, f'{ARTIFACTS_FOLDER}/trained_model.joblib')
print('Trained model serialized successfully!')


# -------------------------------------------------------------------
# Evaluate model
# -------------------------------------------------------------------

y_pred = model.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"\n[INFO] Model Accuracy: {accuracy:.4f}")

report = classification_report(
    y_test,
    y_pred,
    output_dict=True,
)

report_df = pd.DataFrame(report).transpose()
print("\nClassification Report:\n")
print(report_df)

report_df.to_csv(
    f"{METRICS_FOLDER}/classification_report.csv",
    index=True,
)


# -------------------------------------------------------------------
# Save confusion matrix
# -------------------------------------------------------------------

cf = confusion_matrix(y_test, y_pred)

plt.figure(figsize=(10, 6))

sns.heatmap(
    cf,
    xticklabels=["normal", "anomaly"],
    yticklabels=["normal", "anomaly"],
    cmap="Blues",
    annot=True,
    fmt="d",
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title("Confusion Matrix")

plt.savefig(
    f"{METRICS_FOLDER}/confusion_matrix.png",
    bbox_inches="tight",
)

session.close()
print("\n[INFO] Snowflake session closed.")