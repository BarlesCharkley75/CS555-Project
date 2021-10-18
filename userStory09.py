# Birth before death of parents
from CS555Project03 import database, GED_to_dates 
from datetime import date
import unittest
# User Story 09

test1individuals, test1families = database('testfiles/US09test1.ged')
test2individuals, test2families = database('testfiles/US09test2.ged')
test3individuals, test3families = database('testfiles/US09test3.ged')
test4individuals, test4families = database('testfiles/US09test4.ged')
test5individuals, test5families = database('testfiles/US09test5.ged')

#function returns true if birthdate and death date are valid, and death of parents is after birth
#returns false otherwise
def user_story09(individuals, families):
    result = True
    for family in families:
        husband_id = family[3]
        wife_id = family[5]
        children_id_list = family[7]
        for child_id in children_id_list:
            for individual in individuals:
                if (individual[0] == wife_id):
                    wife_deathday = individual[6]
                    wifename = individual[1]
                elif (individual[0] == husband_id):
                    husband_deathday = individual[6]
                    husbname = individual[1]
                elif (individual[0] == child_id):
                    child_birthday = individual[3]
                    childname = individual[1]
            #Only compares earliest parent's death with birth of the child
            if (husband_deathday == 'NA' and wife_deathday == 'NA'):
                continue
            elif (wife_deathday != 'NA' and (husband_deathday == 'NA' or (0 <= GED_to_dates(wife_deathday, husband_deathday)))):
                if (0 > GED_to_dates(child_birthday, wife_deathday)):
                    print(wifename + 'died before the birth of ' + childname)
                    result = False
            elif (0 > GED_to_dates(child_birthday, husband_deathday)):
                print(husbname + 'died before the birth of ' + childname)
                result = False
    return result

class TestBooleanMethods (unittest.TestCase):
    def test_valid(self):
        self.assertEqual(True, user_story09(test1individuals, test1families))
    def test_same_year(self):
        self.assertEqual(False,user_story09(test2individuals, test2families))
    def test_same_month(self):
        self.assertEqual(True,user_story09(test3individuals, test3families))
    def test_same_day(self):
        self.assertEqual(True,user_story09(test4individuals, test4families))
    def test_fail_mult(self):
        self.assertEqual(False,user_story09(test5individuals, test5families))
    

if __name__ == '__main__':
    unittest.main()