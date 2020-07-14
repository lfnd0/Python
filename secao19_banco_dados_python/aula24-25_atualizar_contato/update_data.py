#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

sql = 'UPDATE contato SET nome=%s WHERE id=%s'
args = ('Robbie', 6)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'Updated data: {cursor.rowcount}')
