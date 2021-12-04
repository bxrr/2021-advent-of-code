f = open("input", "r")

count = 0
num = 99999999
for line in f:
    last_num = num
    num = int(line)
    if(last_num < num):
        count += 1

print(count)
