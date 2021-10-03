# user story 31 - authored by Daniel Pekata

from CS555Project03 import database

# we don't need family data for this user story
individuals, discard = database()

singles = []
# check if age > 30 and no spouse. If so, append it to the list of singles
for i in individuals:
    if (i[4] > 30) and (i[8] == "NA"):
        singles.append(i[1])

# print out all singles
print("Singles in the database:\n")
for j in singles:
    print(j)
