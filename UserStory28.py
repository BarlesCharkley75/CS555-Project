# pair programmed between Daniel Pekata and Reilly Fitzgerald
from CS555Project03 import database

individuals, families = database()
sibling_array = []
sibling_list = []
for family in families:
    sibling_list = []
    children = family[7]
    if children == []:
        pass
    for individual in individuals:
        for x in range(len(children)):
            if individual[0] == children[x]:
                sibling_list = sibling_list + [individual]
    if sibling_list != []:
        sibling_array.append(sibling_list)
    
print("Siblings Ordered in Descending Age:")
print("***NOTE: Families with only one child ARE included!***\n")
for i in sibling_array:
    if len(i) == 1:
        print("Siblings in Family " + i[0][7] + ":")
        print(i[0][1])
    if len(i) > 1:
        ages = []
        for x in i:
            ages.append(x[4])
            ages.sort(reverse=True)
        new_i = []
        count = 0
        for x in i:
            if x[4] == ages[count]:
                new_i.append(x)
                count = count + 1
        print("Siblings in family " + new_i[0][7] + ":")
        count = 0
        for x in new_i:
            print(new_i[count][1])
            count = count + 1