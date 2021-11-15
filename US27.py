from CS555Project03 import database, GED_to_day, GED_to_month, GED_to_year
from datetime import date

individuals, discard = database()
#  individual array: # ID(0), NAME(1), GENDER(2), BIRTHDAY(3), AGE(4), ALIVE(5), DEATH(6), CHILD(7), SPOUSE(8)
def US27(individuals):
    today = date.today()
    print(today)
    for person in individuals:
        s = person[3].split()
        day = GED_to_day(s[0])
        month = GED_to_month(s[1])
        year = GED_to_year(s[2])
        age = today.year - int(year) - ((today.month, today.day) < (int(month), int(day)))
        print(person[1] + ": " + str(age) + " years")

US27(individuals)