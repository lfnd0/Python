word = 'paralelepipedo'
for letter in word:
    print(letter, end=', ')
print('the end')

approved = ['Spencer', 'Pavel', 'Logan', 'Danny']
for name in approved:
    print(name)

for position, name in enumerate(approved):
    print(f'{position} - {name}')

days_week = ('sunday', 'monday', 'tuesday', 'wednesday',
             'thursday', 'friday', 'saturday')
for day in days_week:
    print(f'Today is: {day}')

for letter in set('cold'):
    print(letter)

for number in {1, 2, 3, 4}:
    print(number)
