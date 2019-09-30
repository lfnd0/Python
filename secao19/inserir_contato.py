from bd import nova_conexao
from mysql.connector.errors import ProgrammingError

sql = 'INSERT INTO contatos (nome, telefone) VALUES (%s, %s)'
args = ('Gunner', '12345-6789')

with nova_conexao() as conexao:
    try:
        cursor = conexao.cursor()
        cursor.execute(sql, args)
        conexao.commit()
    except ProgrammingError as e:
        print(f'Erro: {e.msg}')
    else:
        print('Resgistro salvo com ID: ', cursor.lastrowid)