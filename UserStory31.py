from CS555Project03 import database
import unittest
# we don't need family data for this user story
individuals, discard = database()

def UserStory31(individuals):
    singles = []
    # check if age > 30 and no spouse. If so, append it to the list of singles
    for i in individuals:
        if (i[4] > 30) and (i[8] == "NA"):
            singles.append(i[1])
    return singles



result = UserStory31(individuals)
# print out all singles
# if len(result) == 0:
#     print("No singles.\n")
# print("Singles in the database:\n")
# for j in result:
#     print(j)

class TestStringMethods(unittest.TestCase):
    # Testing for US01
    def test1(self):
        self.assertEqual(UserStory31([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]), ['Stanley /Thors/'])
    
    def test2(self):
        self.assertEqual(UserStory31([['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@']]), [])

    def test3(self):
        self.assertEqual(UserStory31([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', 'NA'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', 'NA'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]), ['Arthur /Thors/', 'Rose /Krisla/', 'Stanley /Thors/'])
    
    def test4(self):
        self.assertEqual(UserStory31([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 18, True, 'NA', 'NA', 'NA'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', 'NA'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]), ['Rose /Krisla/', 'Stanley /Thors/'])


if __name__ == '__main__':
    unittest.main()