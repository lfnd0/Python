#! python

from math import pi
import sys
import errno


def help():
    print('Execution error.\nCorrect syntax: %s <radius>' %
          (sys.argv[0][-21:]))


def circumference_area(radius):
    return pi * (float(radius) ** 2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)
    else:
        radius = sys.argv[1]
        area = circumference_area(radius)
        print(f'Circumference area is: %.2f' % (area))
