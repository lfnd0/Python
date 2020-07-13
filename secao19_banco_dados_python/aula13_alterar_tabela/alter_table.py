#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

sql = 'ALTER TABLE contato ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY'

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
