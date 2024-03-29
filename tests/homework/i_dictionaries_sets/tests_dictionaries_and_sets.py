import unittest 
from src.homework.i_dictionaries_sets.dictionary import add_inventory, remove_inventory_widget, inventory_dictionary

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