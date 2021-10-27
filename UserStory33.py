from CS555Project03 import database
import unittest

individuals, families = database()
def UserStory33(individuals, families):
    output = []
    for family in families:
        husband_dead = False
        wife_dead = False
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == husband_id):
                husband_dead = individual[5]
            if (individual[0] == wife_id):
                wife_dead = individual[5]
        if (husband_dead == True) and (wife_dead == True):
            children = family[7]
            for child in children:
                output = output + [child]
    return output

# individuals = [['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]
# families = [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]
result = UserStory33(individuals, families)

for i in result:
    print(i + " is an orphan.")

class TestStringMethods(unittest.TestCase):
    # Testing for US33
    def test1(self):
        self.assertEqual(UserStory33([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]), ['@I3@'])
    
    def test2(self):
        self.assertEqual(UserStory33([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', []]]), [])

if __name__ == '__main__':
    unittest.main()