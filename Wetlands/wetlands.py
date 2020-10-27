class Wetlands:

    def __init__(self, name):
        self.attraction_name = name
        self.description = "Fish and other wet things"
        self.animals = list()

    def __str__(self):
        returnstring = f"{self.attraction_name} is where you'll find {self.description}, like \n" 
        for animal in self.animals:
            returnstring += f"* {animal} \n"
        return returnstring

    @property
    def last_critter_added(self):
        return f"{self.animals[-1]}"
