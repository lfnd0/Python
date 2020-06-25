#! python

def double(x):
    return x * 2


def square(x):
    return x ** 2


if __name__ == "__main__":
    functions = [double, square] * 5

    for functions, number in zip(functions, range(1, 11)):
        print(f'The {functions.__name__} of {number} = {functions(number)}')
