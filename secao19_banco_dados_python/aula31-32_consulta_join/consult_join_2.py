#! python

from collections import defaultdict
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
        try:
            cursor.execute(sql)
            contacts = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
    else:
        grouped = defaultdict(list)
        for contact in contacts:
            grouped[contact['description']].append(contact['name'])
        print(grouped)
