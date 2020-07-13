#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS email')
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
