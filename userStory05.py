#US02
from CS555Project03 import database, GED_to_dates 
from datetime import date
import unittest

todays_date = date.today()

test1individuals, test1families = database('testfiles/US05test1.ged')
test2individuals, test2families = database('testfiles/US05test2.ged')
test3individuals, test3families = database('testfiles/US05test3.ged')
test4individuals, test4families = database('testfiles/US05test4.ged')
test5individuals, test5families = database('testfiles/US05test5.ged')

def user_story05(individuals, families):
    for family in families:
        marriage_date = family[1]
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[6] != 'NA' and marriage_date != 'NA'):
                if (individual[0] == wife_id) or (individual[0] == husband_id):
                    marriage_len = GED_to_dates(marriage_date, individual[6])              
                    if marriage_len <= 0:
                        print(individual[1] + " died before they were married in family  " + family[0])
                        return False
                    else:
                        continue
    return True

class TestBooleanMethods (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(True, user_story05(test1individuals, test1families))
    def test_same_month(self):
        self.assertEqual(False,user_story05(test2individuals, test2families))
    def test_same_day(self):
        self.assertEqual(False,user_story05(test3individuals, test3families))
    def test_valid2(self):
        self.assertEqual(True,user_story05(test4individuals, test4families))
    def test_valid3(self):
        self.assertEqual(False,user_story05(test5individuals, test5families))
    

if __name__ == '__main__':
    unittest.main()
        

