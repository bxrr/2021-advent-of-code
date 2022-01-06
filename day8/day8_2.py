def check_in(str1, str2):
    str = str2.split()
    for char in str1:
        if char in str2:
            return True
    return False

def check_in_all(str1, str2):
    if len(str2) < len(str1):
        return False
    else:
        str = str2.split()
        for char in str1:
            if not(char in str2):
                return False
    return True

def exclude(str1, str2):
    for char in str1:
        str2 = str2.replace(char, "")
    return str2

f = open("input", "r")

keys = []
vals = []
for line in f:
    keys.append(line[:line.find("|")-1].split())
    vals.append(line[line.find("|")+1:].split())

for item in keys:
    for i in range(len(item)):
        item[i] = "".join(sorted(item[i]))

for item in vals:
    for i in range(len(item)):
        item[i] = "".join(sorted(item[i]))

sum = 0
for i in range(len(keys)):
    key = keys[i]
    val = vals[i]

    one = ""
    four = ""
    seven = ""
    eight = ""
    t1 = []
    t2 = []
    for item in key:
        if len(item) == 2:
            one = item
        elif len(item) == 3:
            seven = item
        elif len(item) == 5:
            t1.append(item)
        elif len(item) == 4:
            four = item
        elif len(item) == 7:
            eight = item
        elif len(item) == 6:
            t2.append(item)
    
    two = ""
    three = ""
    five = ""
    for item in t1:
        if check_in_all(one, item):
            three = item
        elif check_in_all(exclude(one, four), item):
            five = item
        else:
            two = item
    
    nine = ""
    six = ""
    zero = ""
    for item in t2:
        if check_in_all(four, item):
            nine = item
        elif check_in_all(five, item):
            six = item
        else:
            zero = item
    
    num = ""
    key = [zero, one, two, three, four, five, six, seven, eight, nine]
    for item in val:
        num += str(key.index(item))
    sum += int(num)

print(sum)