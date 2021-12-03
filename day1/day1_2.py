fo = open("input", "r")

f = []
for line in fo:
    f.append(line.replace("\n",""))

sum = []
for i in range(len(f)-2):
    sum.append(int(f[i]) + int(f[i+1]) + int(f[i+2]))

count = 0
last_item = 5951951959
for item in sum:
    if item > last_item:
        count+=1
    last_item = item

print(count)
