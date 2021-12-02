from CS555Project import database, GED_to_day, GED_to_month, GED_to_year
from datetime import date
import unittest

individuals, families = database()

def getByID(id):
    #Implemented to get rid of reused code
    for person in individuals:
        if(person[0] == id):
            return person
        return "Not found"

#  individual array: # ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)
#  family array: ID(0), MARRIED(1), DIVORCED(2), HUSBANDID(3), HUSBANDNAME(4), WIFEID(5), WIFENAME(6), CHILDREN(7)
def US12(fam):
    husb = fam[3]
    wife = fam[5]
    chil = fam[7]
    if(husb == "NA" or wife == "NA" or chil == []):
        return True
    for i in individuals:
        if(i[0] == husb):
            hage = i[4]
        if(i[0] == wife):
            wage = i[4]
    for k in chil:
        for l in individuals:
            if(l[0] == k):
                cage = l[4]
    if((wage - cage >= 60) or (hage - cage >= 80)):
        print("US12: Children older than parents")
        return False
    print("US12: No children older than parents")
    return True


class TestStringMethods(unittest.TestCase):
    def test1(self):
        for family in families:
            self.assertTrue(US12(family))
        

if __name__ == '__main__':
    unittest.main()