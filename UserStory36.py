from CS555Project03 import database, GED_to_day, GED_to_month, GED_to_year
import unittest
from datetime import date
individuals, discard = database()

def GED_DATE(ged_date):
    day = " "
    month = " "
    year = " "
    s = ged_date.split()
    day = GED_to_day(s[0])
    month = GED_to_month(s[1])
    year = GED_to_year(s[2])
    return year, month, day

def diff_dates(date1, date2):
    return abs(date2-date1).days

def UserStory36(individuals):
    output = []
    today = date.today()
    for individual in individuals:
        if (individual[5] == True):
            continue
        year, month, day = GED_DATE(individual[6])
        death = date(int(year), int(month), int(day))
        result = diff_dates(today, death)
        if result < 30:
            output = output + [individual[1]]
    return output

# individuals = [['@I1@', 'Arthur /Thors/', 'M', '19 MAY 1926', 1198, False, '1 NOV 2021', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]

result = UserStory36(individuals)
for i in result:
    print(i + " died in the past 30 days")

class TestStringMethods(unittest.TestCase):
    # Testing for US36
    def test1(self):
        self.assertEqual(UserStory36([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 1198, False, '1 NOV 2021', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]), ['Arthur /Thors/'])
    
    def test2(self):
        self.assertEqual(UserStory36([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]), [])

if __name__ == '__main__':
    unittest.main()