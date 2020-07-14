#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

contact_table = 'CREATE TABLE IF NOT EXISTS contato(nome VARCHAR(50), telefone VARCHAR(40))'
email_table = 'CREATE TABLE email(id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(50))'

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(contact_table)
            cursor.execute(email_table)
        except ProgrammingError as e:
            print(f'Error: {e.msg}')
except ProgrammingError as e:
    print(f'Connection error: {e.msg}')
