import pytest
from Animal import Animal
from AnimalShelter import AnimalShelter

class TestAnimal():
    def setup(self):
        self.cat = Animal(species='dog', weight=8, age=20, name='Baxter')
        self.dupl_cat = Animal(species='cat', weight=10, age=15, name='puss in boots')

    def test_species(self):
        assert self.cat.species == 'DOG'

    def test_setSpecies(self):
        self.cat.setSpecies('cat')
        assert self.cat.species == 'CAT'

    def test_setWeight(self):
        self.cat.setWeight(10)
        assert self.cat.weight == 10

    def test_setAge(self):
        self.cat.setAge(15)
        assert self.cat.age == 15

    def test_setName(self):
        self.cat.setName('Puss in Boots')
        assert self.cat.name == 'PUSS IN BOOTS'

    def test_toString(self):
        assert self.cat.toString() == f"Species: {self.cat.species}, Name: {self.cat.name}, Age: {self.cat.age}," \
                                      f" Weight: {self.cat.weight:.1f}"

def test_eq():
    cat = Animal(species='cat', weight=10, age=15, name='puss in boots')
    dupl_cat = Animal(species='cat', weight=10, age=15, name='puss in boots')
    assert (cat == dupl_cat) is True

class TestAnimalShelter():
    def setup(self):
        self.cat = Animal(species='cat', weight=10, age=15, name='puss in boots')
        self.dog = Animal(species='dog', weight=8, age=20, name='Baxter')
        self.dog2 = Animal(species='dog', weight=14, age=3, name='Marley')
        self.dogpound = AnimalShelter()
    def test_addAnimal1(self):
        self.dogpound.addAnimal(self.dog)
        assert self.dogpound.shelter.get("DOG") != None

    def test_addAnimal2(self):
        self.dogpound.addAnimal(self.dog)
        self.dogpound.addAnimal(self.dog2)
        assert len(self.dogpound.shelter.get("DOG")) == 2

    def test_removeAnimal(self):
        self.dogpound.addAnimal(self.dog)
        self.dogpound.addAnimal(self.dog2)
        self.dogpound.removeAnimal(self.dog)
        assert self.dogpound.shelter.get("DOG") == [self.dog2]

    def test_getAnimalsBySpecies(self):
        self.dogpound.addAnimal(self.dog)
        self.dogpound.addAnimal(self.dog2)
        assert self.dogpound.getAnimalsBySpecies("DOG") == f"Species: DOG, Name: BAXTER, " \
                                                              f"Age: 20, Weight: 8.0\n" \
               f"Species: DOG, Name: MARLEY, Age: 3, Weight: 14.0"

    def test_removeAnimal(self):
        self.dogpound.addAnimal(self.dog)
        assert self.dogpound.doesAnimalExist(self.dog) == True


dogpound = AnimalShelter()
dog = Animal(species='dog', weight=8, age=20, name='Baxter')
dog2 = Animal(species='dog', weight=14, age=3, name='Marley')
dog3 = Animal(species='dog', weight=14, age=3, name='Dave')

# dogpound.addAnimal(dog)
# dogpound.addAnimal(dog2)
# print(dogpound.shelter["DOG"])
# dogpound.addAnimal(dog3)
# dogpound.removeAnimal(dog2)
# for animal in dogpound.shelter["DOG"]:
#     # print(dogpound.shelter["DOG"][0].name)
#     print(animal.name)