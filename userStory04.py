#US02
from CS555Project03 import database, GED_to_dates 
from datetime import date
import unittest

todays_date = date.today()

test1individuals, test1families = database('testfiles/US04test1.ged')
test2individuals, test2families = database('testfiles/US04test2.ged')
test3individuals, test3families = database('testfiles/US04test3.ged')
test4individuals, test4families = database('testfiles/US04test4.ged')
test5individuals, test5families = database('testfiles/US04test5.ged')

def user_story04(families):
    for family in families:
        if (family[2] != 'NA'):
            marriage_date = family[1]
            divorce_date = family[2]
            marriage_len = GED_to_dates(marriage_date, divorce_date) 
            if marriage_len <= 0:
                print("Family: " + family[0] + " was divorced before they were married in family.")
                return False
            else:
                continue
    return True

class TestBooleanMethods (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(True, user_story04(test1families))
    def test_same_month(self):
        self.assertEqual(False,user_story04(test2families))
    def test_same_day(self):
        self.assertEqual(False,user_story04(test3families))
    def test_valid2(self):
        self.assertEqual(False,user_story04(test4families))
    def test_valid3(self):
        self.assertEqual(True,user_story04(test5families))
    

if __name__ == '__main__':
    unittest.main()
        

