from src.utils import *
from src.config import *
from src.train import model_training
from src.evaluate import model_evaluation

# data ingestion
print('STAGE 1: DATA INGESTION')
train_df = data_loader(file_path=train_df_path)
print('[INFO] Data Ingestion Complete')

# feature engineering
print('STAGE 2: FEATURE ENGINEERING')
processed_df = feature_engineering(cleansed_df=train_df)

# feature selection
X_train, X_test, y_train, y_test = data_splitter(processed_df=processed_df)
print('[INFO] Feature Selection and Engineering Complete')

# model training
print('STAGE 3: MODEL TRAINING')
trained_model = model_training(X_train=X_train,
                               X_test=X_test,
                               y_train=y_train,
                               y_test=y_test)

# model evaluation
print('STAGE 4: MODEL EVALUATION')
model_evaluation(X_test=X_test,
                 y_test=y_test,
                 trained_model=trained_model)
print('[INFO] Model Evaluation Complete')
