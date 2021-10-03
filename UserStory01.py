# User story 01, authored by Daniel Pekata
from datetime import date
import unittest

# formats the day for comparison
def GED_to_day(day):
    if day == "1":
        return "01"
    elif day == "2":
        return "02"
    elif day == "3":
        return "03"
    elif day == "4":
        return "04"
    elif day == "5":
        return "05"
    elif day == "6":
        return "06"
    elif day == "7":
        return "07"
    elif day == "8":
        return "08"
    elif day == "9":
        return "09"
    else: return day

# formats the month for comparison
def GED_to_month(month):
    if month == "JAN":
        return "01"
    elif month == "FEB":
        return "02"
    elif month == "MAR":
        return "03"
    elif month == "APR":
        return "04"
    elif month == "MAY":
        return "05"
    elif month == "JUN":
        return "06"
    elif month == "JUL":
        return "07"
    elif month == "AUG":
        return "08"
    elif month == "SEP":
        return "09"
    elif month == "OCT":
        return "10"
    elif month == "NOV":
        return "11"
    else: return "12"

def GED_to_year(year):
    strlen = len(year)
    if strlen == 1:
        return "000" + year
    elif strlen == 2:
        return "00" + year
    elif strlen == 3:
        return "0" + year
    elif strlen == 4:
        return year
    # if the year is 5 or more digits, it takes place in the future.
    # so for simplicity, say the year is 9999, and fail the cases that way.
    else: return "9999"

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