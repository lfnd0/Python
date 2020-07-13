#! python

from mysql.connector import connect

connection = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root'
)

cursor = connection.cursor()
cursor.execute('SHOW DATABASES')

for i, database in enumerate(cursor, start=1):
    print(f'Database {i}: {database[0]}')
