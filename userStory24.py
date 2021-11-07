#User Story 18
#Author - Joseph Mirabile

from datetime import date, datetime
import unittest

todays_date = date.today()
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

# format a GED date for comparison
def GED_to_date(ged_date):
    day = " "
    month = " "
    year = " "
    s = ged_date.split()
    day = GED_to_day(s[0])
    month = GED_to_month(s[1])
    year = GED_to_year(s[2])
    if int(todays_date.month) > int(month):
        return int(int(todays_date.year) - int(year))
    elif int(todays_date.month) == int(month):
        if int(todays_date.day) > int(day):
            return int(int(todays_date.year) - int(year))
        else:
            return int(int(todays_date.year) - int(year)) - 1
    else:
        return int(int(todays_date.year) - int(year)) - 1

def US24(fam):
    samesies = []
    for i in families:
        if (fam == i[0]):
            m = i[1]
            h = i[3]
            w = i[5]
            for j in families:
                if (j[3] == h and j[5] == w):
                    if(j[1] == i[0]):
                        samesies.append(j)
    if (len(samesies) > 0):
        print("US24: List of families with the same spouse names and marriage date as input family")
        return samesies
    else:
        print("US24: No duplicate families with same spouse names and marriage date")
        return "US24: No duplicate families with same spouse names and marriage date"

# contain all of our work in a function so it can easily be exported for user stories later
def database():
    file = open('Guilty-Gear-Family.ged', mode = 'r', encoding = 'utf-8-sig')
    # this is needed for exactly two operations
    data_array = []
    for line in file:
        e = line.split()
        data_array.append(e)
    file.close()
    # for some reason if the file is not closed and opened again then the program becomes weird
    file = open('Guilty-Gear-Family.ged', mode = 'r', encoding = 'utf-8-sig')
    # initialize toggles and overall arrays of data
    toggle_individual = 0
    toggle_family = 0
    individuals_array = []
    family_array = []
    # ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)
    individual_data = [0, 0, 0, 0, 0, True, "NA", "NA", "NA"]
    # ID(0), MARRIED(1), DIVORCED(2), HUSBANDID(3), HUSBANDNAME(4), WIFEID(5), WIFENAME(6), CHILDREN(7)
    family_data = [0, 0, "NA", 0, 0, 0, 0, []]
    for line in file:
        # isolate the values of the level, the tag, and the data in an array
        s = line.split()
        if (s[0] == '2'):
            if(s[1] == 'DATE'):
                # reconstruct the date
                dateval = s[2] + " " + s[3] + " " + s[4]
                if(dateID == 'BIRT'):
                    individual_data[3] = dateval
                    individual_data[4] = GED_to_date(dateval)
                if(dateID == 'DEAT'):
                    individual_data[6] = dateval
                    individual_data[5] = False
                if(dateID == 'MARR'):
                    family_data[1] = dateval
                if(dateID == 'DIV'):
                    family_data[2] = dateval
        if(s[0] == '1'):
            if(s[1] == 'NAME'):
                individual_data[1] = s[2] + " " + s[3]
            if(s[1] == 'SEX'):
                individual_data[2] = s[2]
            # check what type of date we will be looking at
            if(s[1] == 'BIRT'):
                dateID = 'BIRT'
            if(s[1] == 'DEAT'):
                dateID = 'DEAT'
            if(s[1] == 'MARR'):
                dateID = 'MARR'
            if(s[1] == 'DIV'):
                dateID = 'DIV'
            if(s[1] == 'FAMS'):
                individual_data[8] = s[2]
            if(s[1] == 'FAMC'):
                individual_data[7] = s[2]
            if(s[1] == 'HUSB'):
                family_data[3] = s[2]
                for data in data_array:
                    if data[1] == s[2]:
                        nextelem = data_array[data_array.index(data)-len(data_array)+1]
                        family_data[4] = nextelem[2] + " " + nextelem[3]
            if(s[1] == 'WIFE'):
                family_data[5] = s[2]
                for data in data_array:
                    if data[1] == s[2]:
                        nextelem = data_array[data_array.index(data)-len(data_array)+1]
                        family_data[6] = nextelem[2] + " " + nextelem[3]
            if(s[1] == 'CHIL'):
                family_data[7].append(s[2])
        if(s[0] == '0'):
            # if we find another 0 after looking at an individual, we've found all the data
            # about said individual
            if(toggle_individual == 1):
                individuals_array.append(individual_data)
                individual_data = [0, 0, 0, 0, 0, True, "NA", "NA", "NA"]
                toggle_individual = 0
            # if we find another 0 after looking at a family, we've found all the data
            # about said family
            if(toggle_family == 1):
                family_array.append(family_data)
                family_data = [0, 0, "NA", 0, 0, 0, 0, []]
                toggle_family = 0
            # ignore values that have no relevant data
            if(s[1] in ['NOTE', 'HEAD', 'TRLR']):
                pass
            else:
                # indicate if we are looking at an individual or family
                if(s[2] == 'INDI'):
                    toggle_individual = 1
                    individual_data[0] = (s[1])
                if(s[2] == 'FAM'):
                    toggle_family = 1
                    family_data[0] = (s[1])
    return individuals_array, family_array

individuals, families = database()

for i in individuals:
    jan = filter(str.isdigit, i[0])
    ken = "".join(jan)
    po = int(ken)
    i[0] = po

for j in families:
    jan = filter(str.isdigit, j[0])
    ken = "".join(jan)
    po = int(ken)
    j[0] = po

individuals.sort()
families.sort()

for i in individuals:
    i[0] = '@I' + str(i[0]) + '@'

for j in families:
    j[0] = '@F' + str(j[0]) + '@'

print("Individuals:\n")
for i in individuals:
    print(i)
print("Families:\n")
for i in families:
    print(i)

US24('@F1@')

class testCS555Project(unittest.TestCase):

    def test1(self):
        self.assertEqual(US24('@F2@'),"US24: No duplicate families with same spouse names and marriage date")

if __name__ == '__main__':
    unittest.main()