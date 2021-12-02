from datetime import date
import unittest

def US42(dateobj):
    today = date.today()
    if(dateobj > today):
        return False
    if(dateobj.day > 31):
        return False
    if(dateobj.month > 12):
        return False
    if(dateobj.year < 0):
        return False
    if(dateobj.month == 2):
        if (dateobj.year % 4 != 0):
            if dateobj.day > 29:
                return False
            else:
                if dateobj.day > 28:
                    return False
    if(dateobj.month in [4, 6, 9, 11]):
        if dateobj.day > 30:
            return False
    return True

class TestStringMethods(unittest.TestCase):
    def test1(self):
        self.assertTrue(US42(date.today()))
        self.assertTrue(US42(date(2019, 5, 5)))
        

if __name__ == '__main__':
    unittest.main()