# User story 01, authored by Daniel Pekata
from CS555Project03 import GED_to_day, GED_to_month, GED_to_year
from datetime import date
import unittest

# checks if a given date has occured before the present day
def GED_to_date(ged_date):
    temp = 0
    day = " "
    month = " "
    year = " "
    for i in range(0, len(ged_date)):
        if ged_date[i] == " ":
            # get day
            day = ged_date[0:i]
            # format day
            day = GED_to_day(day)
            # save where we are in the string
            temp = i
            break
    for j in range(temp+1, len(ged_date)):
        if ged_date[j] == " ":
            # get month
            month = ged_date[temp:j].strip()
            # format month
            month = GED_to_month(month)
            # get the remainder of the string, which is the year
            year = ged_date[-j+2:]
            year = GED_to_year(year)
            break
    return year + "-" + month + "-" + day

def GED_before_date(ged_date):
    # check if input is a string
    if not isinstance(ged_date, str):
        return False
    # remove the starting part of the ged date, namely the "2 DATE " part
    format_date = ged_date[7:]
    result = GED_to_date(format_date)
    today = str(date.today())
    # compare today's year with the given year
    while True:
        try:
            # if a string that just isn't a date was passed in, it will fail the try/catch and return False
            result_year = int(result[0:4])
            today_year = int(today[0:4])
            break
        except:
            return False
    if result_year > today_year:
        return False
    elif result_year < today_year:
        return True
    # compare today's month with the given month
    while True:
        try:
            # if a string that just isn't a date was passed in, it will fail the try/catch and return False
            result_month = int(result[5:7])
            today_month = int(today[5:7])
            break
        except:
            return False
    if result_month > today_month:
        return False
    elif result_month < today_month:
        return True
    # compare today's day with the given day
    while True:
        try:
            # if a string that just isn't a date was passed in, it will fail the try/catch and return False
            result_day = int(result[8:])
            today_day = int(today[8:])
            break
        except:
            return False
    if result_day > today_day:
        return False
    else: return True


class TestStringMethods(unittest.TestCase):
    # Testing for US01
    # test that a GED date of may 16th, 1923 is valid
    def test1(self):
        self.assertEqual(GED_before_date("2 DATE 16 MAY 1923"), True)
    
    # test that a GED date of may 16th, 2023 is not valid
    def test2(self):
        self.assertEqual(GED_before_date("2 DATE 16 MAY 2023"), False)

    # test that a GED date of sep 25th, 2021 is valid (this is the current day as of testing)
    def test3(self):
        self.assertEqual(GED_before_date("2 DATE 25 SEP 2021"), True)
    
    #test that a GED date of dec 31st, 2021 is not valid 
    def test4(self):
        self.assertEqual(GED_before_date("2 DATE 31 DEC 2021"), False)
    
    # test that a GED date of july 1st, 100 is valid
    def test5(self):
        self.assertEqual(GED_before_date("2 DATE 1 JUL 100"), True)
    # test that a nondate input is considered false
    def test6(self):
        self.assertEqual(GED_before_date(1), False)
    # test that a string that isn't a date returns false
    def test7(self):
        self.assertEqual(GED_before_date("Hello, I am Daniel Pekata"), False)

if __name__ == '__main__':
    unittest.main()