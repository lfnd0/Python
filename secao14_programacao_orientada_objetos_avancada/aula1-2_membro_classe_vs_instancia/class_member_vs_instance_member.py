#! python

class Human:
    # Atributo de classe
    species = 'Homo sapiens'

    def __init__(self, name):
        self.name = name

    def cave(self):
        self.species = 'Homo neanderthalensis'
        # O 'return self' permite o encadeamento entre a instância e a chamada do método
        return self


if __name__ == "__main__":
    logan = Human('Logan')
    # Human.cave(logan)

    # Encadeamento entre a instância 'grokn' e o método 'cave()'
    grokn = Human('Grokn').cave()

    print(f"Human species: {Human.species}")
    print(f"Logan's species: {logan.species}")
    print(f"Grokn's species: {grokn.species}")
