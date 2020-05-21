#! python

my_file = open('..\\aula1_criando_arquivo_CSV\\people.csv')
data = my_file.read()
my_file.close()

for register in data.splitlines():
    print('Name: {}, age: {}'.format(*register.split(',')))
