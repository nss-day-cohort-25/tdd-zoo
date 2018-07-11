import unittest
from habitat import Habitat

test_habitat = Habitat()

class Habitat_test(unittest.TestCase):
  def test_habitat_is_defined(self):
    """ 
    See if the object has been created
    """
    self.assertTrue(test_habitat, {})

  
if __name__ == '__main__':
    unittest.main()
