def result_F1(first, second, third):
    print(f'First -> {first}')
    print(f'Second -> {second}')
    print(f'Third -> {third}')


if __name__ == "__main__":
    podium = {'third': 'S. Vettel',
              'second': 'M. Verstappen',
              'first': 'L. Hamilton'}
    result_F1(**podium)
