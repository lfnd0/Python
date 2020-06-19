#! python

# Seção 14 - Aula 159
class Human:
    species = 'Homo sapiens'

    def __init__(self, name):
        self.name = name

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

    grokn = Neanderthal('Grokn')

    print(f'Evolution from class: {", ".join(Sapiens.all_species())}')
    print(f'Evolution from instance: {", ".join(logan.all_species())}')

    print(f'Is Homo sapiens evolved? {Sapiens.is_evolved()}')
    print(f'Is Homo neanderthalensis evolved? {Neanderthal.is_evolved()}')
    print(f'Is Logan evolved? {logan.is_evolved()}')
    print(f'Is Grokn evolved? {grokn.is_evolved()}')
