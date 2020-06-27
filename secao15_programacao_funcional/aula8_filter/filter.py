#! python

person = [
    {'name': 'George', 'age': 10},
    {'name': 'Spencer', 'age': 12},
    {'name': 'Mary', 'age': 14},
    {'name': 'Logan', 'age': 16},
    {'name': 'Rachel', 'age': 18},
    {'name': 'Scotty', 'age': 20}
]

minors = filter(lambda m: m['age'] < 18, person)
print(f'Minors: {list(minors)}')

bigger_names = filter(lambda b: len(b['name']) >= 7, person)
print(f'Bigger names: {list(bigger_names)}')
