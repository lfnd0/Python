#! python

# Seção 14 - Aula 173
def multiply(x):
    def calculate(y):
        return x * y
    return calculate


if __name__ == "__main__":
    double = multiply(2)
    triple = multiply(3)

    print(double)
    print(triple)

    print(f'Double of 4 is: {double(4)}')
    print(f'Triple of 5 is: {triple(5)}')
