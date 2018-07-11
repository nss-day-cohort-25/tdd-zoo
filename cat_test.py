import unittest
from cat import Cat
from animal import Animal

class cat_testing(unittest.TestCase):

    def test_cat_maker(self):
        meow = Cat()
        self.assertIsInstance(meow, Animal)

if __name__ == '__main__':
    unittest.main()