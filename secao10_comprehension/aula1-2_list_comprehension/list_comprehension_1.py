# [ expressão for item in list if condicional ]
double = [i * 2 for i in range(10)]
print(double)

# Versão "normal"
double = []
for i in range(10):
    double.append(i * 2)
print(double)
