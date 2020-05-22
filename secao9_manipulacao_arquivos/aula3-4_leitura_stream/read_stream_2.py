#! python

my_file = open('..\\aula1_criando_arquivo_CSV\\people.csv')

# Para arquivos grandes
for register in my_file:
    print('Name: {}, age: {}'.format(*register.strip().split(',')))

my_file.close()
