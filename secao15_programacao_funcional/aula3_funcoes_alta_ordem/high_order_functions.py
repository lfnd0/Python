#! python

from my_module.first_class_functions import double, square


def process(title, my_list, function):
    print(f'Processing: {title}')
    for i in my_list:
        print(i, '=>', function(i))


if __name__ == "__main__":
    process('Double of 1-10', range(1, 11), double)
    process('Square of 1-10', range(1, 11), square)
