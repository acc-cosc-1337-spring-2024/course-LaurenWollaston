import unittest 
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget, inventory_dictionary
from src.homework.i_dictionaries_sets.sets import get_students_who_took_prog1_and_prog2, get_students_who_took_prog1_or_prog2, get_students_who_took_prog1_not_prog_2, get_students_who_took_prog2_not_prog_1, prog1Set, prog2Set

class Test_Config(unittest.TestCase):

    def test_addInventory(self):
        add_inventory(inventory_dictionary,'widget_1',10)
        self.assertEqual(10,inventory_dictionary['widget_1']['quantity'] )
    def test_addInventory_2(self):
        add_inventory(inventory_dictionary,'widget_1',25)
        self.assertEqual(35,inventory_dictionary['widget_1']['quantity'] )
    def test_addInventory_3(self):
        add_inventory(inventory_dictionary,'widget_1',-10)
        self.assertEqual(25,inventory_dictionary['widget_1']['quantity'] )
    def test_removeInventoryWidget(self):
        add_inventory(inventory_dictionary,'widget_2',1000)
        remove_inventory_widget(inventory_dictionary,'widget_1')
        self.assertEqual(1,len(inventory_dictionary))
        self.assertTrue('widget_2' in inventory_dictionary)

    def test_studentsWhoTookBoth(self):
        self.assertSetEqual({'Student3'}, get_students_who_took_prog1_and_prog2(prog1Set, prog2Set))
    def test_studentsWhoTookAny(self):
        self.assertSetEqual({'Student1', 'Student2', 'Student3', 'Student4', 'Student5'}, get_students_who_took_prog1_or_prog2(prog1Set, prog2Set))
    def test_studentsWhoTookProg1Only(self):
        self.assertSetEqual({'Student1', 'Student2'}, get_students_who_took_prog1_not_prog_2(prog1Set, prog2Set))
    def test_studentsWhoTookProg2Only(self):
        self.assertSetEqual({'Student4', 'Student5'}, get_students_who_took_prog2_not_prog_1(prog1Set, prog2Set))