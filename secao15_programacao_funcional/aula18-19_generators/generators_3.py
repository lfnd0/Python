#! python

def sequence():
    number = 0
    while True:
        number += 1
        yield number


if __name__ == "__main__":
    my_sequence = sequence()

    for i in range(0, 4):
        print(next(my_sequence))
