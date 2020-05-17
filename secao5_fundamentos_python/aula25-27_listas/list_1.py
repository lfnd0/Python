# help(list)

list_1 = []
print(len(list_1))

list_1.append('Bonnie')
list_1.append('Logan')
print(len(list_1))

list_2 = [1, 2, 'Gunner', 'Spencer', 'Robbie']
print(list_2)

list_2.remove(1)
list_2.remove(2)
print(list_2)

list_2.reverse()
print(list_2)

list_1.append(list_2)
print(list_1)
