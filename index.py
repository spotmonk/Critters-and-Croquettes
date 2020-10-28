from Animals.fish import *
from Animals.land_animals import *
from Animals.snakes import *
from Animals.goose import *
from attractions.pettingzoo import *
from attractions.snakepit import *
from attractions.wetlands import *


miss_Llama = Llama("Lucy", "domestic llama", "afternoon", "Llama Chow", 123568)
mr_Goat = Goat("Geremy", "screaming goat", "morning", "Goat Chow", 5649161)
mr_Donkey = Donkey("Donny", "domestic donkey", "evening", "Donkey Chow", 65465654)
miss_Alpaca = Alpaca("Allie", "wooly alpaca", "afternoon", "Alpaca Chow", 32118324)
miss_Sheep = Sheep("Dolly", "cloned sheep", "morning", "Sheep Chow", 6156261)
mr_Corn_Snake = Corn_Snake("Cornelius", "nope noodle", "Corn_Snake Chow", 5612351)
miss_Gopher_Snake = Gopher_Snake("Gophey", "nope noodle", "Gopher_Snake Chow", 5132153)
mr_California_Kingsnake = California_Kingsnake("Arnold", "nope noodle", "California_Kingsnake Chow", 1235432)
miss_Rosy_Boa = Rosy_Boa("Rose", "nope noodle", "Rosy_Boa Chow", 513516541)
mr_Ball_Python = Ball_Python("Luci", "nope noodle", "Ball_Python Chow", 51321531)
miss_Weather_loach = Weather_loach("Lochie", "freshwater fish", "Weather_loach Chow", 2156315)
mr_Guppy = Guppy("Gupert", "freshwater fish", "Guppy Chow", 6215315)
miss_Tetra = Tetra("Tetty", "freshwater fish", "Tetra Chow", 6543248)
miss_Arrowana = Arrowana("Rowana", "freshwater fish", "Arrowana Chow", 3248365)
mr_Clown = Clown("Nemo", "saltwater fish", "Clown Chow", 7813599)
bob = Goose("Bob", "Canada Goose", "watercress sandwiches", 666)


varmint_village = PettingZoo("Varmint Village", "A Place to cuddle cute animals")
varmint_village.add_animal(miss_Llama)
varmint_village.add_animal(mr_Goat)
varmint_village.add_animal(mr_Donkey)
varmint_village.add_animal(miss_Alpaca)
varmint_village.add_animal(miss_Sheep)

slither_inn = SnakePit("Slither Inn", "a nopery of nope noodles")
slither_inn.add_animal(mr_Corn_Snake)
slither_inn.add_animal(miss_Gopher_Snake)
slither_inn.add_animal(mr_California_Kingsnake)
slither_inn.add_animal(miss_Rosy_Boa)
slither_inn.add_animal(mr_Ball_Python)

water_world = Wetlands("Water World", "a wet place full of wet things")
water_world.add_animal(miss_Weather_loach)
water_world.add_animal(mr_Guppy)
water_world.add_animal(miss_Tetra)
water_world.add_animal(miss_Arrowana)
water_world.add_animal(mr_Clown)



print(varmint_village)
print(slither_inn)
print(water_world)
