#! python

# Seção 15 - Aula 190
def map_2(function, my_list):
    return(function(element) for element in my_list)


if __name__ == "__main__":
    result = map_2(lambda x: x ** 2, [2, 3, 4])
    print(tuple(result))
