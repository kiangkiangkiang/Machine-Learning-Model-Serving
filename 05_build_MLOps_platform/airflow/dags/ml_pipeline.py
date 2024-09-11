from datetime import datetime, timedelta

import requests
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def train_model():
    requests.get("http://training-endpoint:9999/train")


def switch_model():
    requests.get("http://model-endpoint1:9998/change_model")
    requests.get("http://model-endpoint2:9998/change_model")


default_args = {"start_date": datetime.now()}

with DAG(
    dag_id="machine-learning-training-pipeline",
    schedule_interval=None,
    default_args=default_args,
) as dag:
    Training_Data_Update = DummyOperator(task_id="Training_Data_Update")
    Train_Model = PythonOperator(task_id="Train_Model", python_callable=train_model)
    Switch_Latest_Model = PythonOperator(
        task_id="Switch_Latest_Model", python_callable=switch_model
    )
    Training_Data_Update >> Train_Model >> Switch_Latest_Model
