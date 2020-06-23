#! python

class HTMLToStringMixins:
    def __str__(self):
        html = super().__str__().replace('(', '<strong>(').replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Animal:
    def __init__(self, name, pet=True):
        self.name = name
        self.pet = pet

    def __str__(self):
        return self.name + '(pet)' if self.pet else ''


class PersonHTML(HTMLToStringMixins, Person):
    pass


class AnimalHTML(HTMLToStringMixins, Animal):
    pass


if __name__ == "__main__":
    spencer = PersonHTML('Spencer')
    print(spencer)

    toto = AnimalHTML('Toto')
    print(toto)
