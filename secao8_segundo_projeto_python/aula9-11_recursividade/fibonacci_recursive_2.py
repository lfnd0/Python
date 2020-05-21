#! python

def fibonacci(quantity, sequence=(0, 1)):
    return sequence if len(sequence) == quantity else fibonacci(quantity, sequence + (sum(sequence[-2:]),))


if __name__ == "__main__":
    for element in fibonacci(10):
        print(element)
