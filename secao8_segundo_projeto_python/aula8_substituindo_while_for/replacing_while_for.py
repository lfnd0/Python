#! python

def fibonacci(quantity):
    result = [0, 1]

    for _ in range(2, quantity):
        result.append(sum(result[-2:]))
    return result


if __name__ == "__main__":
    for element in fibonacci(10):
        print(element)
