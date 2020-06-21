#! python

class Human:
    species = 'Homo sapiens'

    def __init__(self, name):
        self.name = name
        self._age = None

    @property
    def rational(self):
        raise NotImplementedError('Property not implemented')

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
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

    @property
    def rational(self):
        return False


class Sapiens(Human):
    species = Human.all_species()[-1]

    @property
    def rational(self):
        return True


if __name__ == "__main__":
    anonymous = Human('Logan')

    try:
        print(anonymous.rational)
    except NotImplementedError:
        print('Abstract property')

    logan = Sapiens('Logan')
    print('Name: {}, class: {}, rational: {}'.format(
        logan.name, logan.__class__.__name__, logan.rational))

    grokn = Neanderthal('Grokn')
    print('Name: {}, class: {}, rational: {}'.format(
        grokn.name, grokn.__class__.__name__, grokn.rational))
