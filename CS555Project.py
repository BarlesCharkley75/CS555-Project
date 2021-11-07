from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from prettytable import PrettyTable
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

# format a GED date to get the correct age
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
        if int(todays_date.day) >= int(day):
            return int(int(todays_date.year) - int(year))
        else:
            return int(int(todays_date.year) - int(year)) - 1
    else:
        return int(int(todays_date.year) - int(year)) - 1

# Compares time between two dates, arguments in order of occurence
def GED_to_dates(ged_date1, ged_date2):
    day1 = " "
    month1 = " "
    year1 = " "
    s1 = ged_date1.split()
    day1 = GED_to_day(s1[0])
    month1 = GED_to_month(s1[1])
    year1 = GED_to_year(s1[2])
    day2 = " "
    month2 = " "
    year2 = " "
    s2 = ged_date2.split()
    day2 = GED_to_day(s2[0])
    month2 = GED_to_month(s2[1])
    year2 = GED_to_year(s2[2])
    if int(month2) > int(month1):
        return int(int(year2) - int(year1))
    elif int(month2) == int(month1):
        if int(day2) >= int(day1):
            return int(int(year2) - int(year1))
        else:
            return int(int(year2) - int(year1)) - 1
    else:
        return int(int(year2) - int(year1)) - 1

def getByID(id):
    #Implemented to get rid of reused code
    for person in individuals:
        if(person[0] == id):
            return person
        return "Not found"
# ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)

def US01(ged_date):
    # check if input is a string
    if not isinstance(ged_date, str):
        return False
    # remove the starting part of the ged date, namely the "2 DATE " part
    # format_date = ged_date[7:]
    result = GED_to_date(ged_date)
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

def US02(individuals, families):
    for family in families:
        marriage_date = family[1]
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == wife_id) or (individual[0] == husband_id):
                marriage_age = GED_to_dates(individual[3], marriage_date) #age at the marriage 
                if marriage_age <= 0:
                    print(individual[1] + " was married before they were born in family  " + family[0])
                    return False
                else:
                    continue
    return True

def US03(individuals):
    for i in individuals:
        birth = i[3]
        death = i[6]
        if death != 'NA':
            birthday = datetime.strptime(birth, '%d %b %Y')
            deathday = datetime.strptime(death, '%d %b %Y')
            if birthday > deathday:
                print("US03: Invalid birthday for " + i[0])
                return False
            else:
                return True

def US04(families):
    for family in families:
        if (family[2] != 'NA'):
            marriage_date = family[1]
            divorce_date = family[2]
            marriage_len = GED_to_dates(marriage_date, divorce_date) 
            if marriage_len <= 0:
                print("Family: " + family[0] + " was divorced before they were married in family.")
                return False
            else:
                continue
    return True

def US05(individuals, families):
    for family in families:
        marriage_date = family[1]
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[6] != 'NA' and marriage_date != 'NA'):
                if (individual[0] == wife_id) or (individual[0] == husband_id):
                    marriage_len = GED_to_dates(marriage_date, individual[6])              
                    if marriage_len <= 0:
                        print(individual[1] + " died before they were married in family  " + family[0])
                        return False
                    else:
                        continue
    return True

def US08(families):
    for fam in families:
        print("US08: Children in family: " + str(fam[7]))
        for kid in fam[7]:
            child_array = getByID(kid)
            print("Kid = " + kid)
            print(child_array)
            print("Birthday " + child_array[3])
            print("Married " + str(fam[1]))
            print("Divorced "+ fam[2])
            if(fam[2] == 0):
                if(child_array[3] < fam[1]):
                    return False
            else:
                if (fam[2] != "NA"):
                    if(child_array[3] > (fam[2] + str(relativedelta(months=9)))):
                        return False
    return True


def US09(individuals, families):
    result = True
    for family in families:
        husband_id = family[3]
        wife_id = family[5]
        children_id_list = family[7]
        for child_id in children_id_list:
            for individual in individuals:
                if (individual[0] == wife_id):
                    wife_deathday = individual[6]
                    wifename = individual[1]
                elif (individual[0] == husband_id):
                    husband_deathday = individual[6]
                    husbname = individual[1]
                elif (individual[0] == child_id):
                    child_birthday = individual[3]
                    childname = individual[1]
            #Only compares earliest parent's death with birth of the child
            if (husband_deathday == 'NA' and wife_deathday == 'NA'):
                continue
            elif (wife_deathday != 'NA' and (husband_deathday == 'NA' or (0 <= GED_to_dates(wife_deathday, husband_deathday)))):
                if (0 > GED_to_dates(child_birthday, wife_deathday)):
                    print(wifename + 'died before the birth of ' + childname)
                    result = False
            elif (0 > GED_to_dates(child_birthday, husband_deathday)):
                print(husbname + 'died before the birth of ' + childname)
                result = False
    return result
    

def US10(individuals, families):
    for family in families:
        marriage_date = family[1]
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == wife_id) or (individual[0] == husband_id):
                marriage_age = GED_to_dates(individual[3], marriage_date) #age at the marriage 
                if marriage_age < 14:
                    print(individual[1] + " was under 14 when married in family " + family[0])
                    return False
                else:
                    continue
    return True   

# Checks to see if families have 15 or more children or not
def US15(fam):
    siblings = []
    for i in fam:
        if(i[7] != [] and len(i[7]) > 15):
            siblings.append(i)
    if len(siblings) >= 1:
        print("US15: These families have 15 or more siblings:")   
        for j in siblings:
            print(j)
        return siblings
    else:
        print("US15: No families with 15 or more siblings found")
        return "US15: No families with 15 or more siblings found"

def US17(fam):
    gross = []
    for i in fam:
        paw = i[3]
        maw = i[5]
        for j in i[7]:
            if(j == paw or j == maw):
                gross.append(i)
    if(len(gross) >= 1):
        print("US17: These families have a marriage to a descendant:") 
        for k in gross:
            print(gross)
        return gross
    else:
        print("US17: No families with a marriage to a descendant found")
        return "US17: No families with a marriage to a descendant found"

def US18(fam):
    gotted = []
    for i in fam:
        if len(i[7]) > 1:
            for x in range(len(i[7])):
                for y in range(x + 1, len(i[7])):
                    for z in families:
                        if ((i[7][x] in z[3] or i[7][x] in z[5]) and (i[7][y] in z[3] or i[7][y] in z[5])):
                            gotted.append(i)
                            print("US 18: Found families with marriages between siblings")
                            return gotted
    print("US 18: No families with marriage between siblings")
    return "US 18: No families with marriage between siblings"

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
    if (len(samesies) < 1):
        print("US24: List of families with the same spouse names and marriage date as input family")
        return samesies
    else:
        return "US24: No duplicate families with same spouse names and marriage date"

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

def US25(family):
    for member in family:
        if(member[7] != []):
            for child in member[7]:
                for child2 in member[7]:
                    #Calls to getByID
                    compareTo = getByID(child)
                    compareAgainst = getByID(child2)
                    if(compareTo[1] == compareAgainst[1] and compareTo[3] == compareAgainst[3] and compareTo[0] != compareAgainst[0]):
                        print("US25: Invalid for " + compareTo + " and " + compareAgainst)
                        return False
    print("US25: Valid")
    return True

def US31(individuals):
    singles = []
    # check if age > 30 and no spouse. If so, append it to the list of singles
    for i in individuals:
        if (i[4] > 30) and (i[8] == "NA"):
            singles.append(i[1])
    print("US31: List of singles over 30: ")
    print(singles)
    return singles

def US33(individuals, families):
    output = []
    for family in families:
        husband_dead = False
        wife_dead = False
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == husband_id):
                husband_dead = individual[5]
            if (individual[0] == wife_id):
                wife_dead = individual[5]
        if (husband_dead == True) and (wife_dead == True):
            children = family[7]
            for child in children:
                output = output + [child]
    return output

def US34(individuals, families):
    output = []
    for family in families:
        husband_age = 0
        wife_age = 0
        husband_id = family[3]
        wife_id = family[5]
        for individual in individuals:
            if (individual[0] == husband_id):
                husband_age = individual[4]
            if (individual[0] == wife_id):
                wife_age = individual[4]
        if (max(husband_age, wife_age) > 2 * min(husband_age, wife_age)):
            output = output + [[husband_id, wife_id]]
    return output


# contain all of our work in a function so it can easily be exported for user stories later
def database():
    file = open('example.ged', mode = 'r', encoding = 'utf-8-sig')
    # this is needed for exactly two operations
    data_array = []
    for line in file:
        e = line.split()
        data_array.append(e)
    file.close()
    # for some reason if the file is not closed and opened again then the program becomes weird
    file = open('example.ged', mode = 'r', encoding = 'utf-8-sig')
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

    for i in individuals_array:
        jan = filter(str.isdigit, i[0])
        ken = "".join(jan)
        po = int(ken)
        i[0] = po

    for j in family_array:
        jan = filter(str.isdigit, j[0])
        ken = "".join(jan)
        po = int(ken)
        j[0] = po

    individuals_array.sort()
    family_array.sort()

    for i in individuals_array:
        i[0] = '@I' + str(i[0]) + '@'

    for j in family_array:
        j[0] = '@F' + str(j[0]) + '@'

    return individuals_array, family_array

individuals, families = database()

# if this code is not put into main, every user story that imports database will also run
# this print
if __name__ == "__main__":
    print("Individuals:\n")
    indi_table = PrettyTable(["ID", "Name", "Gender", "Birthday", "Age", "Alive", "Death", "Child", "Spouse"])
    for i in individuals:
        indi_table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8]])
    print(indi_table)
    print("Families:\n")
    fam_table = PrettyTable(["ID", "Married", "Divorced", "Husband ID", "Husband Name", "Wife ID", "Wife Name", "Children"])
    for i in families:
        fam_table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]])
    print(fam_table)

    for i in individuals:
        US01(i[3])
    US02(individuals, families)
    US03(individuals)
    US04(families)
    US05(individuals, families)
    US08(families)
    US09(individuals, families)
    US10(individuals, families)
    US15(families)
    US17(families)
    US18(families)
    US24('@F1@')
    US25(families)
    US31(individuals)
    US33(individuals, families)
    US34(individuals, families)

    class testUserStories(unittest.TestCase):
        def test1(self):
            self.assertEqual(US01("16 MAY 2023"), False)
        def test2(self):
            self.assertEqual(True, US02(individuals, families))
        def test3(self):
            self.assertTrue(US03(individuals))
        def test4(self):
            self.assertEqual(True, US04(families))
        def test5(self):
            self.assertEqual(True, US05(individuals, families))
        def test8(self):
            self.assertTrue(US08(families))
        def test9(self):
            self.assertEqual(True, US09(individuals, families))
        def test10(self):
            self.assertEqual(True, US10(individuals, families))
        def test15(self):
            self.assertEqual(US15([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@']], ['@F2@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I1@']]]), "US15: No families with 15 or more siblings found")
        def test17(self):
            self.assertEqual(US17([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@', '@I8@', '@I9@', '@I10@', '@I11@', '@I12@']], ['@F2@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I1@']]]), "US17: No families with a marriage to a descendant found")
        def test18(self):
            self.assertEqual(US18([['@F1@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I5@', 'Jack-O /Valentine/', ['@I7@'],['@F2@', 0, 'NA', '@I1@', 'Frederick /Bulsara/', '@I2@', 'Aria /Hale/', ['@I6@']], ['@F3@', 0, 'NA', '@I3@', 'Eddie /Bulsara/', '@I4@', 'Millia /Rage/', ['@I3@']]]]), "US 18: No families with marriage between siblings")
        def test24(self):
            self.assertEqual(US24('@F1@'),"US24: No duplicate families with same spouse names and marriage date")
        def test25(self):
            self.assertTrue(US25(families))
        def test31(self):
            self.assertEqual(US31([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, False, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']]), ['Stanley /Thors/'])
        def test33(self):
            self.assertEqual(US33([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 98, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]), ['@I3@'])
        def test34(self):
            self.assertEqual(US34([['@I1@', 'Arthur /Thors/', 'M', '16 MAY 1923', 1198, True, 'NA', 'NA', '@F1@'], ['@I2@', 'Rose /Krisla/', 'F', '7 DEC 1917', 103, True, '15 JUN 2016', 'NA', '@F1@'], ['@I3@', 'Stanley /Thors/', 'M', '12 SEP 1952', 69, True, 'NA', '@F1@', 'NA']], [['@F1@', '6 JAN 1950', '5 SEP 1953', '@I1@', 'Arthur /Thors/', '@I2@', 'Rose /Krisla/', ['@I3@']]]), [['@I1@', '@I2@']])
    
    unittest.main()