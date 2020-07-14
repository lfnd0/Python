#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

select_group = 'SELECT id FROM grupo WHERE descricao=%s'
update_contact = 'UPDATE contato SET grupo_id=%s WHERE nome = %s'
args = {
    'Mary': 'Casa',
    'Robbie': 'Casa',
    'Becca': 'Trabalho',
    'George': 'Trabalho',
    'Anne': 'Trabalho',
    'Scotty': 'Trabalho',
    'Tonny': 'Trabalho'
}

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        for contact, group in args.items():
            cursor.execute(select_group, (group, ))
            group_id = cursor.fetchone()[0]
            cursor.execute(update_contact, (group_id, contact))
            connection.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print('Success')
