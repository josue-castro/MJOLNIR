import os
from dotenv import load_dotenv
load_dotenv()
LOCAL=1
CLOUD=2
db_selector = LOCAL

if db_selector == LOCAL:
    db_user = os.getenv('LOCAL_DB_USER')
    db_pass = os.getenv('LOCAL_DB_PASS')
    db_name = os.getenv('LOCAL_DB_NAME')
    cloud_sql_connection_name = os.getenv('HOST')#os.getenv('CLOUD_SQL_CONNECTION_NAME')
elif db_selector == CLOUD:
    db_user = os.getenv('DB_USER')
    db_pass = os.getenv('DB_PASS')
    db_name = os.getenv('DB_NAME')
    cloud_sql_connection_name = os.getenv('CLOUD_SQL_CONNECTION_NAME')


db_config = {
    'username': "postgres",
    'password': "5458",
    'database': "postgres",
    'host': "35.237.166.44",
    'port': 5432
}
