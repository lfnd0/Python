#! python

from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Calendário em pt-br
setlocale(LC_ALL, 'pt_BR')

months_31 = filter(lambda month: mdays[month] == 31, range(1, 13))
month_names = map(lambda month: month_name[month],  months_31)
join_months = reduce(
    lambda all, name: f'{all}\n - {name}', month_names, 'Months with 31 days:')
print(join_months)

print(
    reduce(
        lambda all, name: f'{all}\n - {name}',
        map(
            lambda month: month_name[month],
            filter(
                lambda month: mdays[month] == 31, range(1, 13)
            )
        ),
        'Months with 31 days:'
    )
)
