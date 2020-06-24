#! python

class SimpleClass:
    counter = 0

    def __init__(self):
        # Funciona da mesma forma que o método 'count'
        # self.__class__.counter += 1
        self.count()

    @classmethod
    def count(cls):
        cls.counter += 1


if __name__ == "__main__":
    in_list = [SimpleClass(), SimpleClass()]
    print(SimpleClass.counter)
