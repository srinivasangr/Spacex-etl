from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='spacex_dbt_pipeline',
    default_args=default_args,
    description='ETL pipeline for SpaceX data using dbt on Redshift',
    schedule_interval='0 */6 * * *',  # Every 6 hours
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=['spacex', 'dbt', 'redshift'],
) as dag:

    dbt_run = BashOperator(
        task_id='run_dbt_transformations',
        bash_command='cd /usr/local/airflow/dags/spacex_pipeline && dbt run --profiles-dir .',
    )

    dbt_test = BashOperator(
        task_id='run_dbt_tests',
        bash_command='cd /usr/local/airflow/dags/spacex_pipeline && dbt test --profiles-dir .',
    )

    dbt_run >> dbt_test







