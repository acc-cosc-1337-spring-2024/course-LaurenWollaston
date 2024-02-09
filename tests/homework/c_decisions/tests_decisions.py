import unittest 
from src.homework.c_decisions.decisions import test_config, get_options_ratio, get_faculty_rating

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

class getOptionsRatio(unittest.TestCase):

    def test_getOptionsRatio_1(self):
        self.assertEqual(0.25, get_options_ratio(5,20))
    
    def test_getOptionsRatio_2(self):
        self.assertEqual(0.5, get_options_ratio(10,20))

class getFacultyRating(unittest.TestCase):

    def test_getFacultyRating_1(self):
        self.assertEqual('EXCELLENT', get_faculty_rating(.91))

    def test_getFacultyRating_2(self):
        self.assertEqual('VERY GOOD', get_faculty_rating(.85))
    
    def test_getFacultyRating_3(self):
        self.assertEqual('GOOD', get_faculty_rating(.71))

    def test_getFacultyRating_4(self):
        self.assertEqual('NEEDS IMPROVEMENT', get_faculty_rating(.66))

    def test_getFacultyRating_5(self):
        self.assertEqual('UNACCEPTABLE', get_faculty_rating(.45))
