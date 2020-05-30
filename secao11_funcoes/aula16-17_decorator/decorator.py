#! python

def log(function):
    def decorator(*args, **kwargs):
        print(f'Function call start: {function.__name__}')
        print(f'args: {args}')
        print(f'kwargs: {kwargs}')

        result = function(*args, **kwargs)

        print(f'Call result: {result}')
        return result

    return decorator


@log
def sum_xy(x, y):
    return x + y


@log
def sub_xy(x, y):
    return x - y


if __name__ == "__main__":
    print(sum_xy(5, 7))
    print(sub_xy(5, y=7))
