f = open("input", "r")
lines = []
for line in f:
    lines.append(line.replace("\n", ""))

o2 = lines.copy()
co2 = lines.copy()

fo2 = []
fco2 = []

for i in range(len(lines[0])):
    temp_o2 = []
    temp_co2 = []

    o2_0 = 0
    o2_1 = 0
    for line in o2:
        if line[i] == "0":
            o2_0 += 1
        else:
            o2_1 += 1

    co2_0 = 0
    co2_1 = 0
    for line in co2:
        if(line[i] == "0"):
            co2_0 += 1
        else:
            co2_1 += 1

    if o2_0 > o2_1:
        for line in o2:
            if line[i] == "0":
                temp_o2.append(line)
    else:
        for line in o2:
            if line[i] == "1":
                temp_o2.append(line)

    if co2_0 > co2_1:
        for line in co2:
            if line[i] == "1":
                temp_co2.append(line)
    else:
        for line in co2:
            if line[i] == "0":
                temp_co2.append(line)

    o2 = temp_o2
    co2 = temp_co2

    if len(o2) == 1:
        fo2 = o2.copy()
    if len(co2) == 1:
        fco2 = co2.copy()

print(fo2)
print(fco2)