from .person import Person


class Salesman(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary
