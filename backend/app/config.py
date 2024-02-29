import pymysql
import os


def get_connection():
    return pymysql.connect(
        host="127.0.0.1",
        port=3800,
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME"),
    )
