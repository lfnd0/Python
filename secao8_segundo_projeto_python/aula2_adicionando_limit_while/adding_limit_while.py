#! python

def fibonacci(limit):
    penult = 0
    last = 1
    
    print(f'{penult}, {last}', end=', ')
    
    while last < limit:
        next_value = penult + last
        print(next_value, end=', ')
        penult = last
        last = next_value


if __name__ == "__main__":
    fibonacci(10)
