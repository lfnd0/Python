product = {'name': 'pen', 'price': 2.99, 'imported': True, 'stock': 100}

for key in product:
    print(f'Key: {key}')

for value in product.values():
    print(f'Value: {value}')

for key, value in product.items():
    print(f'{key}: {value}')
