#! python

from locale import setlocale, LC_ALL
from calendar import mdays, month_name

setlocale(LC_ALL, 'pt_BR')

print('Months with 31 days:')
for month in range(1, 13):
    if mdays[month] == 31:
        print(f'- {month_name[month]}')
