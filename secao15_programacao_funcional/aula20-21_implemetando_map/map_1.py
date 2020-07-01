#! python

# Seção 15 - Aula 189
def map_1(function, my_list):
    for element in my_list:
        yield function(element)


if __name__ == "__main__":
    result = map_1(lambda x: x ** 2, [2, 3, 4])
    print(list(result))
