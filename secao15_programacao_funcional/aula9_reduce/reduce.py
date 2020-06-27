#! python

from functools import reduce

person = [
    {'name': 'George', 'age': 10},
    {'name': 'Spencer', 'age': 12},
    {'name': 'Mary', 'age': 14},
    {'name': 'Logan', 'age': 16},
    {'name': 'Rachel', 'age': 18},
    {'name': 'Scotty', 'age': 20}
]

sum_ages = reduce(lambda ages, a: ages + a['age'], person, 0)
print(f'Sum ages: {sum_ages}')

ages = map(lambda a: a['age'], person)
minors = filter(lambda m: m < 18, ages)
sum_minors = reduce(lambda s_m, a: s_m + a, minors, 0)
print(f'Sum minors: {sum_minors}')
