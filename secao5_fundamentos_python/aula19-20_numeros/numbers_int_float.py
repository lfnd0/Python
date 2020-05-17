print(dir(int))

print(dir(float))

i = 5
print(type(i))

j = 2.5
print(type(j))

print(i + j)
print(i - j)
print(i * j)
print(i / j)

print(j.is_integer())
print(5.0.is_integer())

k = int.__add__(2, 3)
print(k)

x = (-2).__abs__()
print(x)

y = abs(-3)
print(y)

z = (-2.2).__abs__()
print(z)
