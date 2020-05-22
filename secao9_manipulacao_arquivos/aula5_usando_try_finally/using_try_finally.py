#! python

try:
    my_file = open('..\\aula1_criando_arquivo_CSV\\people.csv')

    for register in my_file:
        print('Name: {}, age: {}'.format(register.strip().split(',')))

finally:
    my_file.close()
    print('Closed file!')
