import os

import mlflow
import mlflow.sklearn
import pandas as pd
from mlflow.models import infer_signature
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri("http://localhost:5001")
# mlflow.create_experiment(name="4")
mlflow.set_experiment(experiment_id="4")


mlflow.autolog()
db = load_diabetes()

X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# dataset = mlflow.data.from_pandas(pd.DataFrame(db.data))

# Create and train models. Auto-log in mlflow.
with mlflow.start_run() as run:
    rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
    rf.fit(X_train, y_train)

    # pd.DataFrame(db.data).to_csv("my_training_data.csv")

    # mlflow.log_input(dataset, context="my training data")
    mlflow.log_table(pd.DataFrame(db.data), "my_artifact_file.json")
