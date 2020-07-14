#! python

from database.new_connection_function import new_connection

sql = 'SELECT nome, id FROM contato ORDER BY nome DESC'

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    print('\n'.join(str(contact) for contact in cursor))
