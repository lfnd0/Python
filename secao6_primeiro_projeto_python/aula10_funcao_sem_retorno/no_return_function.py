#! python

from math import pi


def circumference_area(radius):
    calc = pi * (float(radius) ** 2)
    print(f'Circumference area is: %.2f' % (calc))


if __name__ == "__main__":
    radius = input('Entry radius: ')
    circumference_area(radius)
