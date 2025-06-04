import mysql.connector
from mysql.connector import Error

def connector_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="hendra"
        )
        if connection.is_connected():
            db_info = connection.get_server_info()
            print(f"Berhasil Login {db_info}")
            return connection
    except Error as e:
        print(f"gagal {e}")
        return None
    