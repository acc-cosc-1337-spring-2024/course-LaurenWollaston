import unittest 
from src.homework.e_functions.value_return import get_hour, get_minutes, get_seconds, standard_time

class Test_Config(unittest.TestCase):

    def test_getHour(self):
        self.assertEqual(1,get_hour(3800))
        self.assertEqual(1,get_hour(3600))
    
    def test_getMinutes(self):
        self.assertEqual(3,get_minutes(3800))
        self.assertEqual(0,get_minutes(3600))

    def test_getSeconds(self):
        self.assertEqual(20,get_seconds(3800))
        self.assertEqual(0,get_seconds(3600))
    
    def test_printStandardTime(self):
        self.assertEqual('02:14:18',standard_time(1708654458))
        self.assertEqual('02:16:25',standard_time(1708654585))