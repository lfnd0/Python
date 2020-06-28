#! python

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

setlocale(LC_ALL, 'pt_BR')


def months_31(month):
    return mdays[month] == 31


def get_month_names(month):
    return month_name[month]


def join_months(all, name):
    return f'{all}\n - {name}'


print(reduce(join_months, map(get_month_names, filter(
    months_31, range(1, 13))), 'Months with 31 days:'))
