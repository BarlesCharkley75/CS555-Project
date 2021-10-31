from CS555Project03 import database, GED_to_dates 
from datetime import date
import unittest

todays_date = date.today()





test1individuals, test1families = database('testfiles/US10test1.ged')
test2individuals, test2families = database('testfiles/US10test2.ged')
test3individuals, test3families = database('testfiles/US10test3.ged')
test4individuals, test4families = database('testfiles/US10test4.ged')
test5individuals, test5families = database('testfiles/US10test5.ged')

def user_story10(individuals, families):
    for family in families:
        marriage_date = family[1]
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == wife_id) or (individual[0] == husband_id):
                marriage_age = GED_to_dates(individual[3], marriage_date) #age at the marriage 
                if marriage_age < 14:
                    print(individual[1] + " was under 14 when married in family " + family[0])
                    return False
                else:
                    continue
    return True

class TestBooleanMethods (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(True, user_story10(test1individuals, test1families))
    def test_same_year(self):
        self.assertEqual(False,user_story10(test2individuals, test2families))
    def test_same_month(self):
        self.assertEqual(True,user_story10(test3individuals, test3families))
    def test_same_day(self):
        self.assertEqual(True,user_story10(test4individuals, test4families))
    def test_same_month_pass(self):
        self.assertEqual(False,user_story10(test5individuals, test5families))
    

if __name__ == '__main__':
    unittest.main()
        

