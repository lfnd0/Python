#! python

from sqlite3 import connect, ProgrammingError, Row

group_table = """
    CREATE TABLE IF NOT EXISTS grupo(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao VARCHAR(30)
    )
"""

contact_table = """
    CREATE TABLE IF NOT EXISTS contato(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(50),
        telefone VARCHAR(40),
        grupo_id INTEGER,
        FOREIGN KEY(grupo_id) REFERENCES grupo(id)
    )
"""

insert_groups = 'INSERT INTO grupo(descricao) VALUES(?)'

select_groups = 'SELECT id, descricao FROM grupo'

insert_contacts = 'INSERT INTO contato(nome, telefone, grupo_id) VALUES(?, ?, ?)'

select = """
    SELECT grupo.descricao AS grupo, contato.nome AS contato
    FROM contato
    INNER JOIN grupo ON contato.grupo_id=grupo.id
    ORDER BY grupo, contato
"""

try:
    connection = connect(':memory:')
    connection.row_factory = Row
    cursor = connection.cursor()

    cursor.execute(group_table)
    cursor.execute(contact_table)

    cursor.executemany(insert_groups, (('Casa', ), ('Trabalho', )))
    cursor.execute(select_groups)
    groups = {row['descricao']: row['id'] for row in cursor.fetchall()}

    contacts = (
        ('Logan', 701, groups['Casa']),
        ('Spencer', 418, groups['Casa']),
        ('Robbie', 781, groups['Trabalho']),
        ('George', 822, None),
        ('Scotty', 654, None),
        ('Dean', 272, None)
    )

    cursor.executemany(insert_contacts, contacts)
    cursor.execute(select)

    for contact in cursor:
        print(f"Name: {contact['contato']} - Group: {contact['grupo']}")
except ProgrammingError as e:
    print(f'Error: {e.msg}')
