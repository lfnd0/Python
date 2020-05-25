dictionary = {i: i * 2 for i in range(10) if i % 2 == 0}
print(dictionary)

for number, double in dictionary.items():
    print(f'{number} x 2 = {double}')
