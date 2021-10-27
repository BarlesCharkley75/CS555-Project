from CS555Project03 import database
import unittest

individuals, families = database()

def UserStory34(individuals, families):
    output = []
    for family in families:
        husband_age = 0
        wife_age = 0
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == husband_id):
                husband_age = individual[4]
            if (individual[0] == wife_id):
                wife_age = individual[4]
        if (max(husband_age, wife_age) > 2 * min(husband_age, wife_age)):
            output = output + [[husband_id, wife_id]]
    return output

# individuals = [['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 1198, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]
# families = [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]
result = UserStory34(individuals, families)
print(result)
for i in result:
    print(i[0] + " and " + i[1] + " were married with a large age difference.")

class TestStringMethods(unittest.TestCase):
    # Testing for US33
    def test1(self):
        self.assertEqual(UserStory34([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 1198, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]), [['@I1@', '@I2@']])
    
    def test2(self):
        self.assertEqual(UserStory34([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', []]]), [])

if __name__ == '__main__':
    unittest.main()