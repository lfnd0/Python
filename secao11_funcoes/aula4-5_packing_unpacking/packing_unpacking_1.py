def sum_2(a, b):
    return a + b


def sum_3(a, b, c):
    return a + b + c


def sum_values(*numbers):
    my_sum = 0
    for number in numbers:
        my_sum += number
    return my_sum


if __name__ == "__main__":
    print(sum_2(2, 3))

    print(sum_3(2, 4, 6))

    # Packing: parâmetros são "empacotados" dentro de uma tupla
    print(sum_values(1))
    print(sum_values(1, 1))
    print(sum_values(1, 1, 1, 1, 1, 1))

    # Unpacking: parâmetros são "desempacotados" de dentro da tupla/lista
    tuple_numbers = (1, 2, 4)
    print(sum_3(*tuple_numbers))

    list_numbers = [1, 2, 4]
    print(sum_3(*list_numbers))
