#! python

from mysql.connector import connect
from contextlib import contextmanager

parameters = dict(
    host='localhost',
    port=3306,
    user='root',
    passwd='root',
    database='secao19_banco_dados_python'
)


@contextmanager
def new_connection():
    connection = connect(**parameters)
    try:
        yield connection
    finally:
        if(connection and connection.is_connected()):
            connection.close()
