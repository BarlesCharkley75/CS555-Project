import unittest
import datetime
from prettytable import PrettyTable
family = PrettyTable()
family.field_names = ["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"]
from hw4 import US03

class tests(unittest.TestCase):
    def test_1(self):
        print("Test 1")
        self.assertTrue(US03(birthday = datetime.datetime(1900, 1, 1), alive = False, death = datetime.datetime(1984, 4, 20)))
    def test_2(self):
        print("Test 2")
        self.assertFalse(US03(birthday = datetime.datetime(1999, 1, 1), alive = False, death = datetime.datetime(1984, 4, 20)))
    def test_3(self):
        print("Test 3")
        self.assertTrue(US03(birthday = datetime.datetime(1900, 1, 1), alive = False, death = datetime.datetime(1900, 1, 1)))
    def test_4(self):
        print("Test 4")
        self.assertTrue(US03(birthday=datetime.datetime(1900, 1, 1)))
    def test_5(self):
        print("Test 5")
        self.assertFalse(US03(death = datetime.datetime(1984, 6, 9)))



if __name__ == '__main__':
    unittest.main()