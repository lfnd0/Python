#! python

class Human:
    species = 'Homo sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    def get_age(self):
        return self._age

    def set_age(self, age):
        if age < 0:
            raise ValueError('Age cannot be a negative number')
        self._age = age

    def cave(self):
        self.species = 'Homo neanderthalensis'
        return self

    @staticmethod
    def all_species():
        adjectives = ('Habilis', 'Erectus', 'Neanderthalensis', 'Sapiens')
        return ('Australopithecus',) + tuple(f'Homo {adjective}' for adjective in adjectives)

    @classmethod
    def is_evolved(cls):
        return cls.species == cls.all_species()[-1]


class Neanderthal(Human):
    species = Human.all_species()[-2]


class Sapiens(Human):
    species = Human.all_species()[-1]


if __name__ == "__main__":
    logan = Sapiens('Logan')
    logan.set_age(18)
    print(f'Name: {logan.name}, age: {logan.get_age()}')
