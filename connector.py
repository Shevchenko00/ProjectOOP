import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()


def get_read_connection():
    db_config = {
        'host': os.getenv('DB_HOST_R'),
        'user': os.getenv('DB_USER_R'),
        'password': os.getenv('DB_PASSWORD_R'),
        'database': os.getenv('DB_DATA_R')
    }

    return mysql.connector.connect(**db_config)


def get_write_connection():
    host = os.getenv('DB_HOST_W')
    user = os.getenv('DB_USER_W')
    database = os.getenv('DB_DATA_W')
    password = os.getenv('DB_PASSWORD_W')

    db_config = {
        'host': host,
        'user': user,
        'database': database,
        'password': password
    }

    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as err:
        raise RuntimeError(f"Error connecting to the database: {err}")
