import unittest
from animal import Animal
from pangolin import Pangolin

"""
PangolinTest by Raf

Tests Pangolin
"""


class PangolinTest(unittest.TestCase):

    def test_is_pangolin(self):
        pangy = Pangolin()  # creates an instance of Pagolin
        self.assertEqual(pangy.is_pangolin("pangolin"), "pangolin")


if __name__ == '__main__':
    unittest.main()
