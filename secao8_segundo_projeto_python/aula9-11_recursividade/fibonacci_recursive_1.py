#! python

def fibonacci(quantity, sequence=(0, 1)):
    if len(sequence) == quantity:
        return sequence

    return fibonacci(quantity, sequence + (sum(sequence[-2:]),))

if __name__ == "__main__":
    for element in fibonacci(10):
        print(element)
