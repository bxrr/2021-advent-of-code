count = 0
f = open("input", "r")
for line in f:
    key = [2, 4, 3, 7]
    temp = line[line.find("|")+2:].replace("\n","").split(" ")
    for item in temp:
        if len(item) in key: count += 1
print(count)