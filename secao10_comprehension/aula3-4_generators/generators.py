import sys

generator = (i ** 2 for i in range(10) if i % 2 == 0)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))

# "Tamanho" em memória da solução
print(sys.getsizeof(generator))
