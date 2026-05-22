import pandas as pd
from catboost import CatBoostClassifier
from sklearn.metrics import (
    roc_auc_score,
    log_loss,
    classification_report
)


def model_evaluation(
    X_test: pd.DataFrame,
    y_test: pd.Series,
    trained_model: CatBoostClassifier
) -> None:
    '''
    Evaluates the trained CTR prediction model.

    Args:
        X_test: Feature set of test partition
        y_test: Target set of test partition
        trained_model: Trained CatBoost model

    Returns:
        None
    '''


    # Input Validation
    if X_test.empty:
        raise ValueError(
            "X_test is empty."
        )

    if y_test.empty:
        raise ValueError(
            "y_test is empty."
        )

    if len(X_test) != len(y_test):
        raise ValueError(
            "X_test and y_test row counts do not match."
        )

    if trained_model is None:
        raise ValueError(
            "trained_model cannot be None."
        )


    # Prediction
    try:
        y_pred_proba = trained_model.predict_proba(X_test)[:, 1]
        y_pred = trained_model.predict(X_test)

    except Exception as e:
        raise RuntimeError(
            f"Prediction failed: {e}"
        )


    # Evaluation Metrics
    try:
        roc_auc = roc_auc_score(y_test, y_pred_proba)
        logloss = log_loss(y_test, y_pred_proba)

    except Exception as e:
        raise RuntimeError(
            f"Metric calculation failed: {e}"
        )


    # Results
    print('\nPERFORMANCE METRICS')

    print(f'ROC-AUC: {roc_auc:.4f}')
    print(f'Log Loss: {logloss:.4f}')

    print('\nClassification Report:\n')

    print(
        classification_report(
            y_test,
            y_pred
        )
    )