f = open("input", "r")
lines = []
for line in f:
    lines.append(line.replace("\n", ""))
f.close()

count_0 = [0] * len(lines[0])
count_1 = [0] * len(lines[0])

for line in lines:
    for i in range(len(line)-1):
        if line[i] == "0":
            count_0[i] += 1
        else:
            count_1[i] += 1

gamma = ""
epsilon = ""
for i in range(len(lines[0])):
    if count_0[i] > count_1[i]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(epsilon)
print(gamma)