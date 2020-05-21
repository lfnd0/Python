#! python

def print_out(maximum, actual):
    if actual < maximum:
        print(actual)
        print_out(maximum, actual + 1)


print_out(10, 0)
