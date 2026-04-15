# Joseph Gufreda
# Module 5 Programming Assignment - Testing
# From https://realpython.com/python-testing/#testing-your-code

from fractions import Fraction # Imports Fraction type from fractions module
import unittest # Imports unittest

from my_sum import sum # Imports sum from my_sum

class TestSum(unittest.TestCase): # Creates test class inherited from unittest.TestCase
    def test_list_int(self): # Defines test that it can sum a list of integers
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3] # Provides input
        result = sum(data) # Runs test
        self.assertEqual(result, 6) # Assertation
    
    def test_list_fraction(self): # Test that it can sum a list of fractions
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)] # Provides input
        result = sum(data) # Runs test
        self.assertEqual(result, 1) # Assertation

if __name__ == "__main__": # Sets behavior when called directly
    unittest.main()

# At the end of the notebook, describe the test results in your own words.  What do the test results mean?
# The test results show two tests. The first test passes, as 1 + 2 + 3 = 6. The test runs a sum on the three elements and compares it to 6.
# The second test sums three fractions, 1/4 + 1/4 + 2/5. The answer is 9/10, which is not equal to 1. Thus the test fails.