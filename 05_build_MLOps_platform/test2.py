import os

import mlflow
import mlflow.sklearn
import pandas as pd
from mlflow.models import infer_signature
from sklearn.datasets import load_diabetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

mlflow.set_tracking_uri("http://localhost:5001")
mlflow.set_experiment(experiment_id="3")

client = mlflow.tracking.MlflowClient()
# run_id = "81595cc26baf4c93b7ba251df6f3513b"  # 使用實際的 run_id
# local_dir = "./"
# if not os.path.exists(local_dir):
#     os.makedirs(local_dir)

# # 下載 training_data.csv 文件
# client.download_artifacts(run_id, "./my_training_data.csv", local_dir)
# print(f"Artifacts downloaded to {local_dir}")

# mlflow.autolog()
# db = load_diabetes()

# X_train, X_test, y_train, y_test = train_test_split(db.data, db.target)

# # Create and train models. Auto-log in mlflow.
# with mlflow.start_run() as run:
#     rf = RandomForestRegressor(n_estimators=100, max_depth=6, max_features=3)
#     rf.fit(X_train, y_train)

#     pd.DataFrame(db.data).to_csv("my_training_data.csv")
#     mlflow.log_artifact("my_training_data.csv")

#     # 清理本地文件
#     os.remove("my_training_data.csv")

test = client.load_table(
    experiment_id="4",
    artifact_file="my_artifact_file.json",
)
print(123)
