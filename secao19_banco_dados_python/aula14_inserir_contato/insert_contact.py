#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

sql = 'INSERT INTO contato(nome, telefone) VALUES(%s, %s)'
args = ('Logan', '77402-4384')

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'Contact added ID: {cursor.lastrowid}')
