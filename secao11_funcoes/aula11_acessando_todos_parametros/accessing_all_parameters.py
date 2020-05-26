def all_parameters(*args, **kwargs):
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


if __name__ == "__main__":
    all_parameters('a', 'b', 'c')

    all_parameters(1, 2, 3, available=True, value=12.99)

    all_parameters('Tommy', False, [14, 16], size='M', student=True)

    all_parameters(first='John', second='Danny')
    all_parameters('Mary', first='Ellen')
