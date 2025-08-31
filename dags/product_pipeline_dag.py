from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.ingest import fetch_data
from etl.transform import transform_data
from etl.load import load_to_db

default_args = {
    "owner": "airflow",
    "retries": 1
}

with DAG(
    dag_id="product_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args=default_args
) as dag:

    fetch_task = PythonOperator(
        task_id="fetch_data",
        python_callable=fetch_data
    )

    transform_task = PythonOperator(
        task_id="transform_data",
        python_callable=lambda: transform_data("data/raw/products.json")
    )

    load_task = PythonOperator(
        task_id="load_to_db",
        python_callable=lambda: load_to_db("data/processed/products.parquet")
    )

    fetch_task >> transform_task >> load_task