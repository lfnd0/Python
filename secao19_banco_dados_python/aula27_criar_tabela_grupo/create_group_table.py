#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

group_table = 'CREATE TABLE IF NOT EXISTS grupo(id INT AUTO_INCREMENT PRIMARY KEY, descricao VARCHAR(30))'
alter_contact_table_1 = 'ALTER TABLE contato ADD grupo_id INT'
alter_contact_table_2 = 'ALTER TABLE contato ADD FOREIGN KEY(grupo_id) REFERENCES grupo(id)'

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(group_table)
            cursor.execute(alter_contact_table_1)
            cursor.execute(alter_contact_table_2)
        except ProgrammingError as e:
            print(f'Error: {e.msg}')
except ProgrammingError as e:
    print(f'Connection error: {e.msg}')
