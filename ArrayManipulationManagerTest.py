#Handful of testcases for the functions behind /findsameint, /findsharedstr, and /calculateiqr

import unittest
from ArrayManipulationManager import removeSharedIntegers, getSharedString, Iqr

class ArrayManipulationManagerTest(unittest.TestCase):

    def test_ints_removed(self):
        """Are integers removed successfully?"""
        self.assertEqual((removeSharedIntegers([1, 2, 3, 4], [3, 4, 5, 6])), [1, 2])

    def test_return_unchanged(self):
        """Do integers remain if not shared?"""
        self.assertEqual((removeSharedIntegers([1, 2, 3], [4, 5, 6])), [1, 2, 3])

    def test_empty_array_a(self):
        """Does Array A return empty successfully?"""
        self.assertEqual((removeSharedIntegers([], [4, 5, 6])), [])

    def test_return_sharedstring(self):
        """Is a shared list returned successfully?"""
        self.assertEqual((getSharedString(["hello", "world"], ["hello", "earth"])), ["hello"])

    def test_return_nomatch(self):
        """Does the array return empty successfully if no match?"""
        self.assertEqual((getSharedString(["hello", "world"], ["hi", "earth"])), [])

    def test_iqr_calculation(self):
        """Is IQR calculated successfully?"""
        self.assertEqual((Iqr([10, 100, 20, 30, 50, 60])), {"Q1": 20, "Q3": 60, "median": 40})

if __name__ == '__main__':
    unittest.main()