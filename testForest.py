import unittest 
from forest import Forest 

class ForestTest(unittest.TestCase):

    def test_is_forest(self):
        gatheringOfTrees = Forest()
        self.assertEqual(gatheringOfTrees.is_forest("forest"), "forest")

if __name__ == '__main__':
    unittest.main()