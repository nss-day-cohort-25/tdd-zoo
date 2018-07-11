from animal import Animal
from habitat import Habitat

class Dog (Animal, Habitat):
    def __init__(self, name):
        self.name = name
        Animal.__init__(self)
    def speak():
       return "I am a dog and I live in the forrest"
