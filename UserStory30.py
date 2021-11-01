from CS555Project03 import database
from UserStory25 import getByID
import unittest

individuals, families = database()
#  individual array: # ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)
#  family array: ID(0), MARRIED(1), DIVORCED(2), HUSBANDID(3), HUSBANDNAME(4), WIFEID(5), WIFENAME(6), CHILDREN(7)
def US30(families):
    livingmarried = []
    for fam in families:
        hus = getByID(fam[3])
        wife = getByID(fam[5])
        if hus[5]:
            livingmarried.append(fam[4])
        if wife[5]:
            livingmarried.append(fam[6])
    return livingmarried

result = US30(families)

class TestStringMethods(unittest.TestCase):
    def test(self):
        self.assertEqual(US30([['@F1@', 0, 'NA', '@I1@', 'Odin /Burrson/', '@I2@', 'Frigg /Fjorgynndottir/', ['@I5@']], ['@F2@', 0, 'NA', '@I1@', 'Odin /Burrson/', '@I3@', 'Jord /Jorddottir/', ['@I4@']], ['@F3@', '13 JUL 2010', 'NA', '@I4@', 'Thor /Odinson/', '@I7@', 'Sif /Sifdottir/', ['@I8@', '@I9@']], ['@F4@', 0, 'NA', '@I4@', 'Thor /Odinson/', '@I6@', 'Jarnsaxa /Jarnsaxadottir/', []]]), ['Frigg /Fjorgynndottir/', 'Jord /Jorddottir/', 'Thor /Odinson/', 'Sif /Sifdottir/', 'Thor /Odinson/', 'Jarnsaxa /Jarnsaxadottir/'])

if __name__ == '__main__':
    unittest.main()