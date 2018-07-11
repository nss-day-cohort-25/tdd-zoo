from animal import Animal

class Sloth(Animal):
    """ Author: David Paul

        Inherits from : Animal

        Purpose: represent the animal "sloth"
    """
    def __init__(self):
        """ Initialization for Sloths

        """

        super().__init__(self)
        self.habitat = "forest"
        self.toes= 3
        self.color= "gray"