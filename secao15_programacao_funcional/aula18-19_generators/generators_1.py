#! python

def rainbow_colors():
    yield 'red'
    yield 'orange'
    yield 'yellow'
    yield 'green'
    yield 'blue'
    yield 'indigo'
    yield 'violet'


if __name__ == "__main__":
    generator = rainbow_colors()
    print(f'Class: {type(generator)}')

    while True:
        print(next(generator))
