from string import Template

name, age, male, female = 'Sunny', 22, False, True
print('Name: %s, age: %d, male: %r, female: %r' % (name, age, male, female))

product, price = 'Sundae', 1.99
print('Product: %s, price: %.2f' % (product, price))

print('Name: {}, age: {}'.format(name, age))

print(f'Name: {name}, age: {age}')

print(f'{42 + 31}')

my_str = Template('Name: $name, age: $age, male: $male, female: $female')
print(my_str.substitute(name=name, age=age, male=male, female=female))
