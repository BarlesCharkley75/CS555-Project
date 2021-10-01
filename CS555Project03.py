from datetime import date

def arrayData():
    # open given file - look into wildcarding it instead of hardcoding name later
    file = open('example.ged', mode = 'r', encoding = 'utf-8-sig')
    # get list of all lines
    lines = file.readlines()
    file.close()

    ged_array = []
    for line in lines:
        line_array = []
        substring = " "
        for i in range(0, len(line)):
            if line[i] == " ":
                # add each letter of the tag to a substring
                for j in range(2, len(line)):
                    if line[j] == " ":
                        break
                    substring += str(line[j])
                break
        substring = substring.strip()
        rest = line[(len(substring) + 2):].strip()
        # add level
        line_array = line_array + [line[0]]
        # add tag 
        line_array = line_array + [substring]
        # add rest
        line_array = line_array + [rest]
        # add to overall array
        ged_array = ged_array + [line_array]
    return ged_array

data_array = arrayData()
#print(data_array)
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
    if int(todays_date.month) > int(month):
        return int(int(todays_date.year) - int(year)) - 1
    else:
        return int(int(todays_date.year) - int(year))

individuals_list  = []
# go through the newly created array
for e in data_array:
    # initialize all values to defaults
    individual_ID = ''
    individual_name = ''
    individual_gender = ''
    individual_birthdate = ''
    individual_age = ''
    individual_alive = True
    individual_death = 'N/A'
    individual_child = 'N/A'
    individual_spouse = 'N/A'
    individual_array = []
    # if we find an individual:
    if e[2] == 'INDI':
        # get all the values
        individual_ID = e[1]
        thiselem = e
        nextelem = data_array[data_array.index(e)-len(data_array)+1]
        e = nextelem
        # if the level is 0, we've moved on past info for this person
        while e[0] != '0':
            if e[1] == "NAME":
                individual_name = e[2]
            elif e[1] == "SEX": 
                individual_gender = e[2]
            elif e[1] == "BIRT":
                thiselem = e
                nextelem = data_array[data_array.index(e)-len(data_array)+1]
                individual_birthdate = nextelem[2]
                individual_age = GED_to_date(nextelem[2])
            # ********* Make sure only dead people have a DEAT tag **************
            elif e[1] == "DEAT":
                thiselem = e
                nextelem = data_array[data_array.index(e)-len(data_array)+1]
                individual_death = nextelem[2]
                individual_alive = False
            elif e[1] == "FAMS":
                individual_spouse = e[1]
            elif e[1] == "FAMC":
                individual_child = e[1]
            # increment the while loop
            thiselem = e
            nextelem = data_array[data_array.index(e)-len(data_array)+1]
            e = nextelem
        # once we're out of the while, add all our data
        individual_array = individual_array + [individual_ID]  
        individual_array = individual_array + [individual_name]  
        individual_array = individual_array + [individual_gender]
        individual_array = individual_array + [individual_age]
        individual_array = individual_array + [individual_alive]
        individual_array = individual_array + [individual_death] 
        individual_array = individual_array + [individual_child]
        individual_array = individual_array + [individual_spouse]
        individuals_list = individuals_list + [individual_array]  
print("individuals:\n")
for i in individuals_list:
    print(i)
print("\n")           
family_list  = []
# go through the newly created array
for g in data_array:
    family_ID = ''
    family_married = ''
    family_divorced = "N/A"
    family_husband_id = ''
    family_husband_name = ''
    family_wife_id = ''
    family_wife_name = ''
    family_children = []
    family_array = []
    if g[2] == "FAM":
        family_ID = g[1]
        thiselem = g
        nextelem = data_array[data_array.index(g)-len(data_array)+1]
        g = nextelem
        while g[0] != "0":
            if g[1] == "HUSB":
                family_husband_id = g[2]
                for h in data_array:
                    if h[1] == family_husband_id:
                        thiselem = h
                        nextelem = data_array[data_array.index(h)-len(data_array)+1]
                        family_husband_name = nextelem[2]
            elif g[1] == "WIFE":
                family_wife_id = g[2]
                for h in data_array:
                    if h[1] == family_wife_id:
                        thiselem = h
                        nextelem = data_array[data_array.index(h)-len(data_array)+1]
                        family_wife_name = nextelem[2]
            elif g[1] == "CHIL":
                family_children = family_children + [g[2]]
            elif g[1] == "MARR":
                thiselem = g
                nextelem = data_array[data_array.index(g)-len(data_array)+1]
                family_married = nextelem[2]
            elif g[1] == "DIV":
                nextelem = data_array[data_array.index(g)-len(data_array)+1]
                family_divorced = nextelem[2]
            thiselem = g
            nextelem = data_array[data_array.index(g)-len(data_array)+1]
            g = nextelem
        family_array = family_array + [family_ID]
        family_array = family_array + [family_married]
        family_array = family_array + [family_divorced]
        family_array = family_array + [family_husband_id]
        family_array = family_array + [family_husband_name]
        family_array = family_array + [family_wife_id]
        family_array = family_array + [family_wife_name]
        family_array = family_array + [family_children]
        family_list = family_list + [family_array]
print("Families:\n")
for i in family_list:
    print(i)
