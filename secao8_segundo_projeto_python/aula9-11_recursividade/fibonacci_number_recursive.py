#! python

def fibonacci(number):
    if number < 0:
        print('Input invalid!')
    if number == 0:
        return 0
    if number == 1:
        return 1
    else:
        return fibonacci(number - 1) + fibonacci(number - 2)


print(fibonacci(4))
