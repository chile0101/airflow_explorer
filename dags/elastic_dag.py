from airflow import DAG
from airflow.operators.python import PythonOperator
from hooks.elastic.elastic_hook import ElasticHook

from datetime import datetime

def _print_es_info():
    hook = ElasticHook()


with DAG('elastic_dag', start_date=datetime(2022, 1, 1), schedule_interval='@daily'):
    print_es_info = PythonOperator(
        task_id='print_es_info',
        python_callable=_print_es_info()
    )