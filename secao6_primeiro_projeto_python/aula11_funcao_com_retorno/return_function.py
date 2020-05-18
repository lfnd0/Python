#! python

from math import pi


def circumference_area(radius):
    return pi * (float(radius) ** 2)


if __name__ == "__main__":
    radius = input('Entry radius: ')
    area = circumference_area(radius)

    print(f'Circumference area is: %.2f' % (area))
