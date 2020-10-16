class AnimalShelter:
    def __init__(self):
        self.shelter = {}

    def addAnimal(self, animal):
        # Create key:value if key does not exist
        if self.shelter.get(animal.species) is None:
            self.shelter[animal.species] = [animal]
        # Append to list of animals if species exists
        else:
            self.shelter[animal.species].append(animal)

    def removeAnimal(self, animal):
        if self.doesAnimalExist(animal):
                self.shelter[animal.species].remove(animal)
                if len(self.shelter[animal.species]) == 0:
                    del self.shelter[animal.species]            

    def getAnimalsBySpecies(self, species):
        animal_str = ""
        # Return empty string if species does not exist
        if self.shelter.get(species.upper()) is None:
            return animal_str
        else:
            for animal in self.shelter.get(species.upper()):
                animal_str += animal.toString() + "\n"
            return animal_str[:-1]

    def doesAnimalExist(self, animal):
        # If species not in shelter animal does not exist
        if self.shelter.get(animal.species) is None:
            return False
        else:
            for bad_animal in self.shelter[animal.species]:  # Search though list of animals in species
                if animal == bad_animal:
                    return True
