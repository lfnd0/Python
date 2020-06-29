#! python

from functools import reduce
from operator import add

values = (30, 10, 25, 70, 100, 94)

# Abordagem procedural
print(tuple(sorted(values)))

# Lista 'values' não sofreu mudança
print(values)

print(min(values))
print(max(values))

print(sum(values))

# Realiza a soma dos itens na lista
print(reduce(add, values))

# Inverte a sequência dos itens da lista
print(tuple(reversed(values)))
