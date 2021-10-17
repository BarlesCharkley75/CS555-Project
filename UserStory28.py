# pair programmed between Daniel Pekata and Reilly Fitzgerald
from CS555Project03 import database
import unittest

individuals, families = database()
def UserStory28(individuals, families):
    sibling_array = []
    sibling_list = []
    for family in families:
        sibling_list = []
        children = family[7]
        if children == []:
            pass
        for individual in individuals:
            for x in range(len(children)):
                if individual[0] == children[x]:
                    sibling_list = sibling_list + [individual]
        if sibling_list != []:
            sibling_array.append(sibling_list)
    print("Siblings Ordered in Descending Age:")
    print("***NOTE: Families with only one child ARE included!***\n")
    output_max = []
    for i in sibling_array:
        output_min = []
        output_min = output_min + [i[0][7]]
        if len(i) == 1:
            print("Siblings in Family " + i[0][7] + ":")
            print(i[0][1])
            output_min = output_min + [i[0][1]]
        if len(i) > 1:
            ages = []
            for x in i:
                ages.append(x[4])
                ages.sort(reverse=True)
            new_i = []
            count = 0
            for x in i:
                if x[4] == ages[count]:
                    new_i.append(x)
                    count = count + 1
            print("Siblings in family " + new_i[0][7] + ":")
            count = 0
            for x in new_i:
                print(new_i[count][1])
                output_min = output_min + [new_i[count][1]]
                count = count + 1
        output_max = output_max + [output_min]
        return output_max
    
# print(individuals) # [['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]
# print(families) # [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]
result = UserStory28(individuals, families)

class TestStringMethods(unittest.TestCase):
    # Testing for US01
    def test1(self):
        self.assertEqual(UserStory28([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]), [['@F1@', 'Stanley /Thors/']])
    
    def test2(self):
        self.assertEqual(UserStory28([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', []]]), None)



if __name__ == '__main__':
    unittest.main()