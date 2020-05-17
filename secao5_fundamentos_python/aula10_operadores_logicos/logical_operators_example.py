sale = 1000
salary = 4000
cost = 3967

positive_sale = sale > 0
controlled_cost = salary - cost >= 0.2 * salary

target = positive_sale and controlled_cost
print(target)
