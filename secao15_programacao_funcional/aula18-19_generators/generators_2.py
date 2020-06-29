#! python

from generators_1 import rainbow_colors

if __name__ == "__main__":
    generator = rainbow_colors()

    for color in generator:
        print(color)

    print('Finish')
