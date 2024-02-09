import unittest
from src.examples.b_input_proc_output.input_process_output import test_config, floatingPointDivision

class Test_Config(unittest.TestCase):

    def test_configuration(self):
        self.assertEqual(True, test_config())

class floatingPointDivision(unittest.TestCase):

    def test_floatingPointDivision_1(self):
        self.assertEqual(5, floatingPointDivision(50,10))