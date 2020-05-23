#! python

with open('..\\aula1_criando_arquivo_CSV\\people.csv') as my_file:

    with open('people.txt', 'w') as output:
        for register in my_file:
            people = register.strip().split(',')
            print('Name: {}, age: {}'.format(*people), file=output)

if my_file.closed:
    print('Closed input file!')

if output.closed:
    print('Closed output file!')
