f = open("input", "r")
lines = []
for line in f:
    lines.append(line.replace("\n", ""))
f.close()

o2 = lines.copy()
co2 = lines.copy()

# final lists
fo2 = []
fco2 = []

for i in range(len(lines[0])):
    temp_o2 = []
    temp_co2 = []

    # get number of 0 and 1 in current o2 list
    o2_0 = 0
    o2_1 = 0
    for line in o2:
        if line[i] == "0":
            o2_0 += 1
        else:
            o2_1 += 1

    # get number of 0 and 1 in current co2 list
    co2_0 = 0
    co2_1 = 0
    for line in co2:
        if(line[i] == "0"):
            co2_0 += 1
        else:
            co2_1 += 1

    # append to o2 list based on which whether 0 or 1 is most common
    if o2_0 > o2_1:
        for line in o2:
            if line[i] == "0":
                temp_o2.append(line)
    else:
        for line in o2:
            if line[i] == "1":
                temp_o2.append(line)

    # append to co2 list based on which whether 0 or 1 is most common
    if co2_0 > co2_1:
        for line in co2:
            if line[i] == "1":
                temp_co2.append(line)
    else:
        for line in co2:
            if line[i] == "0":
                temp_co2.append(line)

    # set parent list to temp list in order to reiterate through the list and find next values
    o2 = temp_o2
    co2 = temp_co2

    # check if any of the lists have reached their target length and finalize the list if so
    if len(o2) == 1:
        fo2 = o2.copy()
    if len(co2) == 1:
        fco2 = co2.copy()

# print finalized lists
print(fo2)
print(fco2)