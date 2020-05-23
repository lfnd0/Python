import csv

with open(r'../aula1_criando_arquivo_CSV/people.csv') as entry:

    for people in csv.reader(entry):
        print('Name: {}, age: {}'.format(*people))
