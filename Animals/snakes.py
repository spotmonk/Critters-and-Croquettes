from Animals.animals import Animal
from datetime import date

class Corn_Snake(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True  
        self.food = food
    


class Gopher_Snake(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True  
        self.food = food
    

class California_Kingsnake(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True  
        self.food = food
    

class Rosy_Boa(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True  
        self.food = food
    

class Ball_Python(Animal):

    def __init__(self, name, species, food, chip_number):
        super().__init__(name, species, food, chip_number)
        self.slithering = True  
        self.food = food
