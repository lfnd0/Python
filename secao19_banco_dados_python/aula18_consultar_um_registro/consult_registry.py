#! python

from database.new_connection_function import new_connection

sql = 'SELECT nome, telefone FROM contato'

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())
