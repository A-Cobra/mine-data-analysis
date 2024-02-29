import pymysql
import os


def get_connection():
    return pymysql.connect(
        host="database",
        port=3306,
        user="root",
        password="",
        db="mine",
    )
