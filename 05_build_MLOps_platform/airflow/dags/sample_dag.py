from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator


def sample_task():
    print("Triggered by PostgreSQL change")


default_args = {"start_date": datetime(2023, 1, 1)}

with DAG(dag_id="sample_dag", default_args=default_args, schedule_interval=None) as dag:
    start = DummyOperator(task_id="start")
    trigger_task = PythonOperator(task_id="trigger_task", python_callable=sample_task)
    start >> trigger_task
