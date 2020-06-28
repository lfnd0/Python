#! python

def factorial(n):
    return n * (factorial(n - 1) if (n - 1) > 1 else 1)


if __name__ == "__main__":
    print(f'10! = {factorial(10)}')
