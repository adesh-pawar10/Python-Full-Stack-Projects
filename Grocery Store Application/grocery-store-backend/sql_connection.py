import mysql.connector
from mysql.connector import pooling
import os
from dotenv import load_dotenv

load_dotenv()

connection_pool = None

def get_sql_connection():
    global connection_pool
    if connection_pool is None:
        try:
            connection_pool = mysql.connector.pooling.MySQLConnectionPool(
                pool_name="grocery_store_pool",
                pool_size=10,
                host=os.getenv('DB_HOST'),
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                database=os.getenv('DB_NAME')
            )
        except mysql.connector.Error as err:
            print("Database connection error:", err)
            raise
    return connection_pool.get_connection()

# Context manager to automatically handle connection and cursor cleanup
from contextlib import contextmanager

@contextmanager
def managed_connection():
    conn = get_sql_connection()
    try:
        yield conn
    finally:
        if conn.is_connected():
            conn.close()
