from CS555Project03 import database, GED_to_day, GED_to_month, GED_to_year
from datetime import date
import unittest

individuals, discard = database()
#  individual array: # ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)
def US27(individuals):
    today = date.today()
    agedict = {}
    # print(today)
    # print(individuals)
    for person in individuals:
        s = person[3].split()
        day = GED_to_day(s[0])
        month = GED_to_month(s[1])
        year = GED_to_year(s[2])
        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
        agedict[person[1]] = age
        print(person[1] + ": " + str(age) + " years")
    return agedict

US27(individuals)

class TestStringMethods(unittest.TestCase):
    def test1(self):
        agedict = US27([['@I1@', 'Odin /Burrson/', 'M', '3 FEB 1964', 57, False, '15 OCT 2018', 'NA', '@F2@'], ['@I2@', 'Frigg /Fjorgynndottir/', 'F', '6 MAR 1954', 67, True, 'NA', 'NA', '@F1@'], ['@I3@', 'Jord /Jorddottir/', 'F', '14 JUN 1954', 67, True, 'NA', 'NA', '@F2@'], ['@I4@', 'Thor /Odinson/', 'M', '29 OCT 1986', 35, True, 'NA', '@F2@', '@F4@'], ['@I5@', 'Baldr /Odinson/', 'M', '23 OCT 1990', 31, True, 'NA', '@F1@', 'NA'], ['@I6@', 'Jarnsaxa /Jarnsaxadottir/', 'F', '9 JAN 1980', 41, False, '8 MAY 2004', 'NA', '@F4@'], ['@I7@', 'Sif /Sifdottir/', 'F', '5 SEP 1987', 34, True, 'NA', 'NA', '@F3@'], ['@I8@', 'Modi /Thorson/', 'M', '28 NOV 2011', 9, True, 'NA', '@F3@', 'NA'], ['@I9@', 'Thrud /Thordottir/', 'F', '12 JAN 2016', 5, True, 'NA', '@F3@', 'NA']])
        self.assertEqual(agedict['Odin /Burrson/'], 57)
        self.assertEqual(agedict['Frigg /Fjorgynndottir/'], 67)
        self.assertEqual(agedict['Jord /Jorddottir/'], 67)
        self.assertEqual(agedict['Thor /Odinson/'], 35)

if __name__ == '__main__':
    unittest.main()