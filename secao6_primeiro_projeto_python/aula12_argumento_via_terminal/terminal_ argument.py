#! python

from math import pi
import sys


def circumference_area(radius):
    return pi * (float(radius) ** 2)


if __name__ == "__main__":
    radius = sys.argv[1]
    area = circumference_area(radius)

    print(f'Circumference area is: %.2f' % (area))
