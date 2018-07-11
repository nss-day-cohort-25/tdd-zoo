import unittest
from cd_arctic import Arctic

arctic = Arctic()

class test_arctic(unittest.TestCase):

    def test_arctic_is_habitat(self):
        """
            test to return the name of the class
        """
        self.assertEqual(arctic.return_name(), "arctic")

if __name__ == '__main__':
    unittest.main()