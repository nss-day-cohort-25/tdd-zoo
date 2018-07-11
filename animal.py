class Animal():

    def __init__(self):
        self.size = ""
        self.food = ""
        self.legs = 4
        self.male = False
        self.female = True

    def say_something(self, awesome_string_sound):
        """
        author: rachael babcock

        arguments: takes in self and 1 string that can be any string
        """
        print(awesome_string_sound)
        return awesome_string_sound