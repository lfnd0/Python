#! python

def fibonacci(limit):
    result = [0, 1]

    while result[-1] < limit:
        result.append(result[-2] + result[-1])
    return result


if __name__ == "__main__":
    for element in fibonacci(10):
        print(element)
