#! python

from math import pi
import sys
import errno


class ColorTerminal():
    ERRO = '\033[91m'
    DEFAULT = '\033[0m'


def help():
    print('Execution error.\nCorrect syntax: %s <radius>' %
          (sys.argv[0][-26:]))


def circumference_area(radius):
    return pi * (float(radius) ** 2)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        help()
        sys.exit(errno.EPERM)

    elif not sys.argv[1].isnumeric():
        help()
        print(ColorTerminal.ERRO +
              'The radius must be a numeric value!' + ColorTerminal.DEFAULT)
        sys.exit(errno.EPERM)

    else:
        radius = sys.argv[1]
        area = circumference_area(radius)
        print(f'Circumference area is: %.2f' % (area))
