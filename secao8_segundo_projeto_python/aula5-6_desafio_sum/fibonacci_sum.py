#! python

def fibonacci(limit):
    result = [0, 1]

    while result[-1] < limit:
        result.append(sum(result[-2:]))
    return result


if __name__ == "__main__":
    for element in fibonacci(10):
        print(element)
