#! python

from database.new_connection_function import new_connection

sql = "SELECT nome, telefone FROM contato WHERE telefone='77402-4384'"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    for contact in cursor:
        print(contact)
