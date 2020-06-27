#! python

purchases = (
    {'quantity': 2, 'price': 10},
    {'quantity': 3, 'price': 20},
    {'quantity': 4, 'price': 30}
)


def calculate_total_price(purchase):
    return purchase['quantity'] * purchase['price']


total = tuple(map(calculate_total_price, purchases))

print(f'Total prices: {list(total)}')
print(f'Grand total: {sum(total)}')
