import unittest
from dog import Dog

class DogTest(unittest.TestCase):

    def test_dog_speak_returns_string(self):
        self.assertEqual(Dog.speak(), "I am a dog and I live in the forrest")

    def test_dog_has_property_name(self):
        self.assertTrue(Dog("Rover").name)

    def test_dog_receives_parameter_name(self):
        karma = Dog("Karma")
        self.assertEqual(karma.name, "Karma")

    def test_dog_receives_legs_from_animal(self):
        karma = Dog("Karma")
        self.assertEqual(karma.legs, 4)

if __name__ == '__main__':
    unittest.main()
