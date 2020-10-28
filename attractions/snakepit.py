from .attraction import Attraction
from movements import slithering

class SnakePit(Attraction):

    def __init__(self, name, description):
      super().__init__(name, description)

    # Number 1: Duck typing check
    def add_animal_pythonic(self, animal):
        try:
            if animal.slither_speed > -1:
                self.animals.append(animal)
                print(f"{animal} now lives in {self.attraction_name}")
        except AttributeError as ex:
            print(f'{animal} doesn\'t slither, so please do not put it in the {self.attraction_name} attraction.')

    # Number 2: Actual typing check
    def add_animal_type_check(self, animal):
        if isinstance(animal, slithering):
            self.animals.append(animal)
            print(f"{animal} now lives in {self.attraction_name}")
        else:
            print(f'{animal} doesn\'t slither, so please do not try to put it in the {self.attraction_name} attraction.')
