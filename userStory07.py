#US07
from CS555Project03 import database, GED_to_dates 
from datetime import date
import unittest

todays_date = date.today()

test1individuals, test1families = database('testfiles/US07test1.ged')
test2individuals, test2families = database('testfiles/US07test2.ged')
test3individuals, test3families = database('testfiles/US07test3.ged')
test4individuals, test4families = database('testfiles/US07test4.ged')
test5individuals, test5families = database('testfiles/US07test5.ged')

def user_story07(individuals):
    for individual in individuals:
        if (individual[4] != 'NA'):              
            if individual[4] >= 150:
                print(individual[1] + " lived to be greater than 150")
                return False
            else:
                continue
        else:
            return False
    return True

class TestBooleanMethods (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(True, user_story07(test1individuals))
    def test_same_month(self):
        self.assertEqual(False,user_story07(test2individuals))
    def test_same_day(self):
        self.assertEqual(False,user_story07(test3individuals))
    def test_valid2(self):
        self.assertEqual(False,user_story07(test4individuals))
    def test_valid3(self):
        self.assertEqual(True,user_story07(test5individuals))
    

if __name__ == '__main__':
    unittest.main()
        