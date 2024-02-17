import unittest 
from src.homework.d_repetition.repetition import get_factorial

class getFactorial(unittest.TestCase):

    def test_getFactoral_1(self):
        self.assertEqual(24, get_factorial(4))
    
    def test_getFactoral_2(self):
        self.assertEqual(120, get_factorial(5))

    def test_getFactoral_3(self):
        self.assertEqual(720, get_factorial(6))