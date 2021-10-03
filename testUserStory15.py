import unittest

import userStory15

class testUserStory15(unittest.TestCase):

    def test1(self):
        self.assertEqual(userStory15.US15([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@']], ['@F2@', 0, 'NA', '@I1@', 
'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I1@']]]), "US15: No families with 15 or more siblings found")
   
    def test2(self):
        self.assertEqual(userStory15.US15([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@']], ['@F2@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 0, '@I4@', 0, ['@I1@']]]), "US15: No families with 15 or more siblings found")
    
    def test3(self):
        self.assertEqual(userStory15.US15([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@']], ['@F2@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I1@']]]),[['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@', '@I13@', '@I14@', '@I15@', '@I16@', '@I17@', '@I18@', '@I19@', '@I20@', '@I21@', '@I22@', '@I23@', '@I24@']]])

if __name__ == '__main__':
    unittest.main()