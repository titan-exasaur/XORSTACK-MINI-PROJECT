import pandas as pd
from catboost import CatBoostClassifier
from src.config import *


def model_training(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.Series,
    y_test: pd.Series
) -> CatBoostClassifier:
    '''
    Trains a CatBoost CTR prediction model.

    Args:
        X_train: Training feature dataframe
        X_test: Testing feature dataframe
        y_train: Training target series
        y_test: Testing target series

    Returns:
        CatBoostClassifier: Trained CatBoost model
    '''

    
    # Input validation
    

    if X_train.empty or X_test.empty:
        raise ValueError(
            "X_train or X_test is empty."
        )

    if y_train.empty or y_test.empty:
        raise ValueError(
            "y_train or y_test is empty."
        )

    if len(X_train) != len(y_train):
        raise ValueError(
            "X_train and y_train row counts do not match."
        )

    if len(X_test) != len(y_test):
        raise ValueError(
            "X_test and y_test row counts do not match."
        )

    # Ensure categorical columns exist
    missing_cat_features = [
        col for col in cat_features
        if col not in X_train.columns
    ]

    if missing_cat_features:
        raise ValueError(
            f"Missing categorical features: {missing_cat_features}"
        )

    # Convert categorical columns to string
    for col in cat_features:
        X_train[col] = X_train[col].astype(str)
        X_test[col] = X_test[col].astype(str)

    
    # Model Initialization
    model = CatBoostClassifier(
        iterations=iterations,
        learning_rate=learning_rate,
        depth=depth,
        loss_function=loss_function,
        eval_metric=eval_metric,
        verbose=verbose,
        class_weights=class_weights
    )

    print('[INFO] Model Training Started...')

    
    # Model Training
    model.fit(
        X_train,
        y_train,
        cat_features=cat_features,
        eval_set=(X_test, y_test)
    )

    print('[INFO] Model Training Completed...')

    return model