#! python

from mysql.connector import connect

connection = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root'
)

print(connection)
