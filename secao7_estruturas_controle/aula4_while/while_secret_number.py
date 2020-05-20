from random import randint

entry_number = -1
secret_number = randint(0, 9)

while entry_number != secret_number:
    entry_number = int(input('Enter a number: '))

print("Congratulations! Secret number's {}!" .format(secret_number))
