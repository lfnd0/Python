#! python

from mysql.connector.errors import ProgrammingError
from database.new_connection_function import new_connection

sql = """
    SELECT
        grupo.descricao AS description,
        contato.nome AS name
    FROM contato
    INNER JOIN grupo ON contato.grupo_id=grupo.id
    ORDER BY description, name
"""

with new_connection() as connection:
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute(sql)
        contacts = cursor.fetchall()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        for contact in contacts:
            print(f"{contact['description']}: {contact['name']}")
