class Animal:
    def __init__(self, species: str = None, weight: float = None, age: int = None, name: str = None):
        self.species = species.upper() if type(species) is str else None
        self.weight = weight
        self.age = age
        self.name = name.upper() if type(name) is str else None

    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = weight

    def setAge(self, age):
        self.age = age

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return f"Species: {self.species}, Name: {self.name}, Age: {self.age}, Weight: {self.weight:.1f}"

    # Define deep equality
    def __eq__(self, other):
        return (self.species == other.species and self.weight == other.weight and self.age == other.age and
                self.name == other.name)
