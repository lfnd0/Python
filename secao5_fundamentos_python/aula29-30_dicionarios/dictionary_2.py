person = {'name': 'Richard', 'age': 18, 'courses': ['React', 'React native']}

person['age'] = 17
person['courses'].append('Node')
print(person)

person.pop('age')
print(person)

person.update({'age': 17, 'gender': 'M'})
print(person)

del person['courses']
print(person)

person.clear()
print(person)
