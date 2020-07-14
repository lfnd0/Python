#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

sql = 'INSERT INTO contato(nome, telefone) VALUES(%s, %s)'
args = (
    ('Becca', '70173-4864'),
    ('George', '41874-2438'),
    ('Anne', '78151-9605'),
    ('Scotty', '82222-4763'),
    ('David', '27205-7290'),
    ('Mary', '40063-3110'),
    ('Tonny', '49156-5886')
)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        print(f'Added contacts: {cursor.rowcount}')
