#! python

from database.new_connection_function import new_connection

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute('SHOW TABLES')

for i, tables in enumerate(cursor, start=1):
    print(f'Table {i}: {tables[0]}')
