class Animal():

    def __init__(self):
        self.size = ""
        self.food = ""
        self.legs = 4
        self.male = False
        self.female = True

    def say_something(self, awesome_string_sound):
        print(awesome_string_sound)
        return awesome_string_sound