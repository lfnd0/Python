#! python

def sum_ab(a, b):
    def sum_c(c):
        return a + b + c
    return sum_c


sum_5 = sum_ab(1, 3)

print(sum_5(1))

print(sum_ab(1, 3)(5))
