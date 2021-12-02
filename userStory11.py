#No Bigamy
#US11
from CS555Project03 import database, GED_to_dates 
from itertools import combinations
from datetime import date
import unittest

todays_date = date.today()

test1individuals, test1families = database('testfiles/US11test1.ged')
test2individuals, test2families = database('testfiles/US11test2.ged')
test3individuals, test3families = database('testfiles/US11test3.ged')
test4individuals, test4families = database('testfiles/US11test4.ged')
test5individuals, test5families = database('testfiles/US11test5.ged')

def user_story11( families):
    allmarriagepairs = list(combinations(families, 2))
    for pair in allmarriagepairs:
        divorce_date1=pair[0][2]
        divorce_date2 = pair[1][2]
        marriage_date1=pair[0][1]
        marriage_date2 = pair[1][1]
        husband1=pair[0][3]
        husband2=pair[1][3]
        wife1=pair[0][5]
        wife2=pair[1][5]
        if husband1 == husband2 or wife1 == wife2:
            if GED_to_dates(marriage_date1, marriage_date2) < 0: #marriage 2 happened first
                if divorce_date2 == 'NA':
                    print("Bigamy occured in families " + pair[0][0] + " and " + pair[1][0])
                    return False
                elif (divorce_date1 != 'NA' and GED_to_dates(marriage_date2, divorce_date1) <= 0):
                    print("Bigamy occured in families " + pair[0][0] + " and " + pair[1][0])
                    return False
                elif (divorce_date2 != 'NA' and GED_to_dates(divorce_date2, marriage_date1) <= 0):
                    print("Bigamy occured in families " + pair[0][0] + " and " + pair[1][0])
                    return False
            else:
                if divorce_date1 == 'NA':
                    print("Bigamy occured in families " + pair[0][0] + " and " + pair[1][0])
                    return False
                elif (divorce_date1 != 'NA' and GED_to_dates(divorce_date1, marriage_date2) <= 0):
                    print("Bigamy occured in families " + pair[0][0] + " and " + pair[1][0])
                    return False
                elif (divorce_date2 != 'NA' and GED_to_dates(marriage_date1, divorce_date2) <= 0):
                    print("Bigamy occured in families " + pair[0][0] + " and " + pair[1][0])
                    return False
    return True

class TestBooleanMethods (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(True, user_story11(test1families))
    def test_same_month(self):
        self.assertEqual(False,user_story11(test2families))
    def test_same_day(self):
        self.assertEqual(False,user_story11(test3families))
    def test_valid2(self):
        self.assertEqual(False,user_story11(test4families))
    def test_valid3(self):
        self.assertEqual(True,user_story11(test5families))
    

if __name__ == '__main__':
    unittest.main()
        