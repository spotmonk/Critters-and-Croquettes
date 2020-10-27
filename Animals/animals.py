from datetime import date
   
class Animal:
     
    def __init__(self, name, species, food, chip_number):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.food = food
        self.__chip_number = chip_number

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, number):
        pass

    def __str__(self):  
        return f"{self.name} is a {self.species}"
