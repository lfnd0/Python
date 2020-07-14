#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

sql = 'SELECT * FROM contato LIMIT %s OFFSET %s'
args = (3, 2)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        contacts = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        for contact in contacts:
            print(f'{contact[2]:2d} - {contact[0]:8s} Telephone: {contact[1]}')
