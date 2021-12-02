#US02
from CS555Project03 import database, GED_to_dates 
from datetime import date
import unittest

todays_date = date.today()

test1individuals, test1families = database('testfiles/US02test1.ged')
test2individuals, test2families = database('testfiles/US02test2.ged')
test3individuals, test3families = database('testfiles/US02test3.ged')
test4individuals, test4families = database('testfiles/US02test4.ged')
test5individuals, test5families = database('testfiles/US02test5.ged')

def user_story02(individuals, families):
    for family in families:
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == wife_id) or (individual[0] == husband_id):
                marriage_date = family[1]
                birthday = individual[3]
                marriage_age = GED_to_dates(birthday, marriage_date) #age at the marriage 
                if marriage_age <= 0:
                    print(individual[1] + " was married in family  " + family[0] + " before they were born")
                    return False
                else:
                    continue
    return True

class TestBooleanMethods (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(True, user_story02(test1individuals, test1families))
    def test_same_month(self):
        self.assertEqual(False,user_story02(test2individuals, test2families))
    def test_same_day(self):
        self.assertEqual(False,user_story02(test3individuals, test3families))
    def test_before_either(self):
        self.assertEqual(False,user_story02(test4individuals, test4families))
    def test_valid2(self):
        self.assertEqual(True,user_story02(test5individuals, test5families))
    

if __name__ == '__main__':
    unittest.main()
        

