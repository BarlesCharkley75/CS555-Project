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
def US12(family):
    print(family)
    today = date.today()
    # father_birthday = getByID(family[3])[3].split()
    # mother_birthday = getByID(family[5])[3].split()
    # for ind in individuals:
    #     if ind[0] == '@I2@':
    #         print(ind)
    mother = getByID(family[5])
    father = getByID(family[3])
    father_birthday = father[3].split()
    mother_birthday = mother[3].split()
    mday = GED_to_day(mother_birthday[0])
    mmonth = GED_to_month(mother_birthday[1])
    myear = GED_to_year(mother_birthday[2])
    fday = GED_to_day(father_birthday[0])
    fmonth = GED_to_month(father_birthday[1])
    fyear = GED_to_year(father_birthday[2])
    mother_age = today.year - int(myear) - ((today.month, today.day) < (int(mmonth), int(mday)))
    father_age = today.year - int(fyear) - ((today.month, today.day) < (int(fmonth), int(fday)))
    for child in family[7]:
        child_birthday = getByID(child)
        cday = GED_to_day(child[0])
        cmonth = GED_to_month(child[1])
        cyear = GED_to_year(child[2])
        child_age = today.year - int(cyear) - ((today.month, today.day) < (int(cmonth), int(cday)))
        if(father_age-child_age >= 80 or mother_age-child_age>=60):
            return False
    return True


class TestStringMethods(unittest.TestCase):
    def test1(self):
        for family in families:
            self.assertTrue(US12(family))
        

if __name__ == '__main__':
    unittest.main()