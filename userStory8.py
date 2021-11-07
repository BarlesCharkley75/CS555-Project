from CS555Project import database
from dateutil.relativedelta import relativedelta
import datetime

individuals, families = database()
#  individual array: # ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)
#  family array: ID(0), MARRIED(1), DIVORCED(2), HUSBANDID(3), HUSBANDNAME(4), WIFEID(5), WIFENAME(6), CHILDREN(7)

def getByID(id):
    for person in individuals:
        if(person[0] == id):
            return person
    return "Not found"
# ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)

def US08(families):
    for fam in families:
        print("US08: Children in family: " + str(fam[7]))
        for kid in fam[7]:
            child_array = getByID(kid)
            print("Kid = " + kid)
            print(child_array)
            print("Birthday " + child_array[3])
            print("Married " + str(fam[1]))
            print("Divorced "+ fam[2])
            if(fam[2] == 0):
                if(child_array[3] < fam[1]):
                    return False
            else:
                if (fam[2] != "NA"):
                    if(child_array[3] > (int(fam[2]) + relativedelta(months=9))):
                        return False
    return True

US08(families)