a = {1, 2, 3}
print(type(a))

a = set('python')
print(a)

print('1' in a, 4 not in a)

print({1, 2, 3} == {3, 3, 2, 1})

# Operations

set_1 = {1, 2}
set_2 = {2, 3}

print(set_1.union(set_2))
print(set_1.intersection(set_2))

set_1.update(set_2)
print(set_1)

print(set_2 <= set_1)
print(set_1 >= set_2)

print({1, 2, 3} - {2})
print(set_1 - set_2)

set_1 -= {2}
print(set_1)
