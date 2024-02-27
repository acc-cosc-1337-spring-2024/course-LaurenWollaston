import unittest 
from src.homework.h_strings.strings import get_dna_compliment, get_hamming_distance

class Test_Config(unittest.TestCase):

    def test_getDnaCompliment(self):
        self.assertEqual('ACCGGGTTTT', get_dna_compliment('AAAACCCGGT'))

    def test_getHammingDistance(self):
        self.assertEqual(7, get_hamming_distance('GAGCCTACTAACGGGAT ','CATCGTAATGACGGCCT '))