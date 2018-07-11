import unittest
from cd_arctic import Arctic

arctic = Arctic()

class test_arctic(unittest.TestCase):

    def test_arctic_is_habitat(self):
        self.assertEqual(arctic.return_name(), "arctic")

if __name__ == '__main__':
    unittest.main()