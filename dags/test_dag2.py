from airflow import DAG
from airflow.operators.bash import BashOperator
 
from datetime import datetime
 
with DAG('parallel_dag_test_delete', start_date=datetime(2022, 1, 1), 
    schedule_interval='@daily', catchup=False) as dag:
 
    extract_a = BashOperator(
        task_id='extract_a',
        bash_command='echo ANDA!!!'
    )
 
    extract_b = BashOperator(
        task_id='extract_b',
        bash_command='sleep 1'
    )
 
    load_a = BashOperator(
        task_id='load_a',
        bash_command='sleep 1'
    )
 
    load_b = BashOperator(
        task_id='load_b',
        bash_command='sleep 1'
    )
 
    transform = BashOperator(
        task_id='transform',
        bash_command='sleep 1'
    )
 
    extract_a >> load_a
    extract_b >> load_b
    [load_a, load_b] >> transform