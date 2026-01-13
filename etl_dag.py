from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from app.etl import process

def run():
    process('sample.csv')

dag=DAG('etl_dag',start_date=datetime(2024,1,1),schedule='@daily')
PythonOperator(task_id='etl',python_callable=run,dag=dag)
