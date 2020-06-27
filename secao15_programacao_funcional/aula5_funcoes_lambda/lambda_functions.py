#! python

purchases = (
    {'quantity': 2, 'price': 10},
    {'quantity': 3, 'price': 20},
    {'quantity': 4, 'price': 30}
)

total = tuple(
    map(
        lambda purchase: purchase['quantity'] * purchase['price'], purchases
    )
)

print(f'Total prices: {list(total)}')
print(f'Grand total: {sum(total)}')
