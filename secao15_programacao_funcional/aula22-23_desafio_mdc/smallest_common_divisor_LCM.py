#! python

def LCM(numbers):
    def calculate(divider):
        return divider if sum(map(lambda x: x % divider, numbers)) == 0 else calculate(divider - 1)
    return calculate(min(numbers))


if __name__ == "__main__":
    print(LCM([21, 7]))
    print(LCM([125, 40]))
    print(LCM([9, 564, 66, 3]))
    print(LCM([55, 22]))
    print(LCM([15, 150]))
    print(LCM([7, 9]))
