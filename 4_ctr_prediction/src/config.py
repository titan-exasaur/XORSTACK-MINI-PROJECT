# File paths
train_df_path = 'data/avazu-ctr-prediction/train.csv'

# Catboost Hyperparameters
iterations=500
learning_rate=0.05
depth=8
loss_function="Logloss"
eval_metric="AUC"
verbose=2
class_weights=[1, 5]

# other parameters
test_size=0.2
random_state=42

# Features for Feature Selection
features = [
    'hour_of_day', 'day_of_week', 'weekend_flag',
    'banner_pos',
    'site_category', 'app_category', 'site_domain', 'app_domain',
    'device_type', 'device_conn_type', 'device_model',
    'C1', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21']

# Features for Catboost
cat_features = [
    'banner_pos',
    'site_category', 'app_category', 'site_domain', 'app_domain',
    'device_type', 'device_conn_type', 'device_model',
    'C1', 'C14', 'C15', 'C16', 'C17', 'C18', 'C19', 'C20', 'C21'
]

# Target column
target = 'click'