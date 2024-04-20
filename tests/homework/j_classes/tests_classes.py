import unittest 
import src.homework.j_classes.class_a as diceClass
class Test_Config(unittest.TestCase):

    def test_getRolledValue_1(self):
        dice = diceClass.die()
        dice.roll()
        self.assertTrue(0<dice.get_rolled_value()<=6)

    def test_getRolledValue_2(self):
        dice = diceClass.die()
        dice.roll()
        self.assertTrue(0<dice.get_rolled_value()<=6)
    
    def test_getRolledValue_3(self):
        dice = diceClass.die()
        dice.roll()
        self.assertTrue(0<dice.get_rolled_value()<=6)

    def test_getRolledValue_4(self):
        dice = diceClass.die()
        dice.roll()
        self.assertTrue(0<dice.get_rolled_value()<=6)
        
    def test_getRolledValue_5(self):
        dice = diceClass.die()
        dice.roll()
        self.assertTrue(0<dice.get_rolled_value()<=6)