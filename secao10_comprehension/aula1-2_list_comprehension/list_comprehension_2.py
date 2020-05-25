# [ expressão for item in list if condicional ]
double_pair_numbers = [i * 2 for i in range(10) if i % 2 == 0]
print(double_pair_numbers)

# Versão "normal"
double_pair_numbers = []
for i in range(10):
    if i % 2 == 0:
        double_pair_numbers.append(i * 2)
print(double_pair_numbers)
