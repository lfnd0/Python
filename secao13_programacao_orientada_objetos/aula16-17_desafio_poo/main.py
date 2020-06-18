from datetime import datetime
from store import Client, Salesman, Purchase


def main():
    client = Client('George', 22)
    salesman = Salesman('Scotty', 36, 1000)
    purchase_1 = Purchase(client, datetime.now(), 512)
    purchase_2 = Purchase(client, datetime(2020, 6, 10), 256)
    client.register_purchase(purchase_1)
    client.register_purchase(purchase_2)

    print(f'Client: {client}', '(adult)' if client.is_adult() else '')
    print(f'Salesman: {salesman}')

    total_value = client.total_purchases()
    amount_purchases = len(client.purchases)
    print(f'Total: {total_value} in {amount_purchases} purchases')
    print(f'Last purchase: {client.get_date_last_purchase()}')


if __name__ == "__main__":
    main()
