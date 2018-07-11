from animal import Animal

class Cat(Animal):

    def __init__(self, animal="cat"):
        self.animal = animal
        Animal().__init__()
