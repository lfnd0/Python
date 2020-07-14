#! python

from database.new_connection_function import new_connection

sql = 'SELECT nome, telefone FROM contato WHERE nome LIKE %s'

with new_connection() as connection:
    name = input('Search for contact: ')
    args = (f'%{name}%', )

    cursor = connection.cursor()
    cursor.execute(sql, args)

    for contact in cursor:
        print(contact)
