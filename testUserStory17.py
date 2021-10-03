import unittest

import userStory17

class testUserStory17(unittest.TestCase):

    def test1(self):
        self.assertEqual(userStory17.US17([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@']], ['@F2@', 0, 'NA', '@I1@', 
'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I1@']]]), "US17: No families with a marriage to a descendant found")
   
    def test2(self):
        self.assertEqual(userStory17.US17([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@']], ['@F2@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 0, '@I4@', 0, ['@I1@']]]), "US17: No families with a marriage to a descendant found")

    def test3(self):
        self.assertEqual(userStory17.US17([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@']], ['@F2@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I3@']]]),[['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I3@']]])
if __name__ == '__main__':
    unittest.main()