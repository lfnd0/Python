#! python

from mysql.connector import connect

connection = connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='root'
)

cursor = connection.cursor()
cursor.execute('CREATE DATABASE IF NOT EXISTS secao19_banco_dados_python')
