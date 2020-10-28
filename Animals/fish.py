from Animals.animals import Animal
from datetime import date

class Weather_loach(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)    
        self.swimming = True
        self.food = food

class Guppy(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)    
        self.swimming = True
        self.food = food

class Tetra(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)    
        self.swimming = True
        self.food = food

class Arrowana(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)    
        self.swimming = True
        self.food = food
            

class Clown(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)    
        self.swimming = True
        self.food = food
