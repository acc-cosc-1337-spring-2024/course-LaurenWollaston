import unittest
'''
the file in /tests/homework/b_in_proc_out/tests_in_proc_out
has the test functions
'''
# from tests.homework.b_in_proc_out import tests_in_proc_out
# from tests.homework.d_repetition import tests_repetition
# from tests.homework.e_functions import tests_functions
# from tests.homework.h_strings import tests_strings
# from tests.homework.i_dictionaries_sets import tests_dictionaries_and_sets
from tests.homework.j_classes import tests_classes

suite = unittest.TestLoader().loadTestsFromModule(tests_classes)
unittest.TextTestRunner(verbosity=2).run(suite)
