from bd import nova_conexao
from mysql.connector.errors import  ProgrammingError

sql = 'INSERT INTO contatos (nome, telefone) VALUES (%s, %s)'
args = (
    ('Logan', '12345-6789'),
    ('Robb', '12345-6789'),
    ('Cay', '98765-4321'),
    ('George', '98765-4321'),
    ('Spencer', '98765-4321'),
)
with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.executemany(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print(f'Quantidades de resgistros salvos: {cursor.rowcount}')