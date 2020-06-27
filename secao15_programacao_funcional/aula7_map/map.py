#! python

list_1 = [1, 2, 3]

double = map(lambda num: num * 2, list_1)
print(list(double))

list_2 = [
    {'name': 'Logan', 'age': 16},
    {'name': 'Daniel', 'age': 18},
    {'name': 'George', 'age': 20},
]

names = map(lambda n: n['name'], list_2)
print(f'Names: {list(names)}')

ages = map(lambda a: a['age'], list_2)
print(f'Ages: {list(ages)}')

total_sum_ages = map(lambda a: a['age'], list_2)
print(f'Total sum ages: {sum(total_sum_ages)}')

phrases = map(
    lambda p: f"{p['name']} is {p['age']} years old", list_2)
print(list(phrases))
