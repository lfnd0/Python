#! python

class RGB:
    def __init__(self):
        self.colors = ['red', 'green', 'blue']

    def __iter__(self):
        return self

    def __next__(self):
        try:
            return self.colors.pop()
        except IndexError:
            raise StopIteration()


if __name__ == "__main__":
    colors = RGB()
    print(next(colors))
    print(next(colors))
    print(next(colors))

    try:
        print(next(colors))
    except StopIteration:
        print('Finish')

    for color in RGB():
        print(color)
