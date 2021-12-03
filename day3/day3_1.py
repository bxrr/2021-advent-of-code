def peek_line(f):
    pos = f.tell()
    line = f.readline()
    f.seek(pos)
    return line

f = open("input", "r")
line_len = len(peek_line(f).replace("\n", ""))
count_0 = [0] * line_len
count_1 = [0] * line_len

for line in f:
    for i in range(len(line)-1):
        if line[i] == "0":
            count_0[i] += 1
        else:
            count_1[i] += 1

gamma = ""
epsilon = ""
for i in range(line_len):
    if count_0[i] > count_1[i]:
        gamma += "0"
        epsilon += "1"
    else:
        gamma += "1"
        epsilon += "0"

print(epsilon)
print(gamma)