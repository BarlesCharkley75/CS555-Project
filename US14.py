from CS555Project03 import database
import unittest

discard, families = database()

def US14(family):
    # ID(0), MARRIED(1), DIVORCED(2), HUSBANDID(3), HUSBANDNAME(4), WIFEID(5), WIFENAME(6), CHILDREN(7)
    if len(family[7]) > 5:
        return False
    return True

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertTrue(US14(['@F1@', 0, 'NA', '@I1@', 'Odin /Burrson/', '@I2@', 'Frigg /Fjorgynndottir/', ['@I5@']]))
        self.assertFalse(US14(['@F1@', 0, 'NA', '@I1@', 'Odin /Burrson/', '@I2@', 'Frigg /Fjorgynndottir/', ['@I5@', '@I4@', '@I10@', '@I8@', '@I9@', '@I10@', '@I13']]))

if __name__ == '__main__':
    unittest.main()