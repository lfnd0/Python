#! python

# Seção 6 - Aula 61

from math import pi

radius = input('Entry radius: ')
circumference_area = pi * (float(radius) ** 2)

print(f'Circumference area is: %.2f' % (circumference_area))

print('Name module: ', __name__)
