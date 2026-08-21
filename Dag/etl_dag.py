from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


def run_etl():
    print("ETL pipeline is running...")


with DAG(
    dag_id="simple_etl",
    start_date=datetime(2026, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    etl_task = PythonOperator(
        task_id="run_etl",
        python_callable=run_etl,
    )