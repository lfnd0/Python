#! python

with open('..\\aula1_criando_arquivo_CSV\\people.csv') as my_file:

    for register in my_file:
        print('Name: {}, age: {}'.format(*register.strip().split(',')))

if my_file.closed:
    print('Closed file!')
