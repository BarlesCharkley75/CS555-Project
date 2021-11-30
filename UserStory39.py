from CS555Project03 import database, GED_to_day, GED_to_month, GED_to_year
import unittest
from datetime import date

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

individuals, families = database()
def UserStory39(families):
    output = []
    for family in families:
        anniversary = family[1]
        today = date.today()
        todaystr = str(today)
        thisyear = todaystr[0:4]
        year, month, day = GED_DATE(anniversary)
        anniversary = date(int(thisyear), int(month), int(day))
        result = diff_dates(today, anniversary)
        if result < 30:
            output = output + [[family[4], family[6]]]
    return output

# individuals = [['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]
# families = [['@F1@', '12 DEC 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]
result = UserStory39(families)
print(families)
for i in result:
    print(i[0] + " and " + i[1] + " have an anniversary coming up!")


class TestStringMethods(unittest.TestCase):
    # Testing for US39
    def test1(self):
        self.assertEqual(UserStory39([['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]), [])
    
    def test2(self):
        self.assertEqual(UserStory39([['@F1@', '12 DEC 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]), [['Arthur /Thors/', 'Rose /Krisla/']])

if __name__ == '__main__':
    unittest.main()