import unittest 
from src.homework.d_repetition.repetition import get_factorial, sum_odd_numbers

class getFactorial(unittest.TestCase):

    def test_getFactoral_1(self):
        self.assertEqual(24, get_factorial(4))
    
    def test_getFactoral_2(self):
        self.assertEqual(120, get_factorial(5))

    def test_getFactoral_3(self):
        self.assertEqual(720, get_factorial(6))

class sumOddNumbers(unittest.TestCase):
    def test_sumOddNumbers_1(self):
        self.assertEqual(16, sum_odd_numbers(7))
    def test_sumOddNumbers_2(self):
        self.assertEqual(25, sum_odd_numbers(9))
    def test_sumOddNumbers_3(self):
        self.assertEqual(25, sum_odd_numbers(10))