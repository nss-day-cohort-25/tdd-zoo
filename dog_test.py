import unittest
from dog import Dog

class DogTest(unittest.TestCase):

    def test_dog_speak(self):
        self.assertEqual(Dog.speak(), "I am a dog and I live in the forrest")

if __name__ == '__main__':
    unittest.main()
