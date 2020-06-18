OLDER_AGE = 18


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        if not self.age:
            return self.name
        return f'{self.name} ({self.age} years)'

    def is_adult(self):
        return (self.age or 0) > OLDER_AGE
