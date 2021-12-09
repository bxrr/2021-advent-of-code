f = open("input", "r")
fish = f.read().replace("\n","").split(",")
for i in range(len(fish)):
    fish[i] = [int(fish[i]), 1]

def simulate_day(fish_list, day):
    temp = [8, 0]
    for i in range(len(fish_list)):
        if fish_list[i][0] == 0:
            fish_list[i][0] = 6
            temp[1] += fish_list[i][1]
        else:
            fish_list[i][0] -= 1
    fish_list.append(temp)

    if day == 256:
        return fish_list
    else:
        return simulate_day(fish_list, day+1)

fish = simulate_day(fish, 1)
sum = 0
for nums in fish:
    sum += nums[1]
print(sum)