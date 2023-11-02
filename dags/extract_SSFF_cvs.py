from datetime import datetime
from airflow import DAG
from airflow.contrib.hooks.ssh_hook import SSHHook
from airflow.contrib.operators.sftp_operator import SFTPOperator



default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 11, 2),
    'retries': 1,
}

dag = DAG(
    'sftp_data_extraction',
    default_args=default_args,
    description='Extract file from Success Factor SFTP',
    schedule_interval='@once',
)

# Establecer la conexión SSH
ssh_hook = SSHHook(ssh_conn_id=sftp_conn_id)
ssh_hook.no_host_key_check = True

# Define la tarea para extraer el archivo del SFTP
extract_file_task = SFTPOperator(
    task_id='extract_file',
    ssh_hook=ssh_hook,
    local_filepath='RRHH/ssff.csv',  # Ruta donde se guardará el archivo localmente
    remote_filepath='/Interfaces/03_Production/SFSF_DATA_WAREHOUSE/DataWarehouse_20231031.csv',
    operation='get',
    create_intermediate_dirs=True,
    dag=dag,
)

extract_file_task