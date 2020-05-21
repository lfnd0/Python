#! python

def fibonacci(limit):
    penult = 0
    last = 1
    
    print(f'{penult}, {last}', end=', ')
    
    while last < limit:
        penult, last = last, penult + last
        print(last, end=', ')


if __name__ == "__main__":
    fibonacci(10)
