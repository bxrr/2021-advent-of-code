f = open("input", "r")
fish = f.read().replace("\n","").split(",")
for i in range(len(fish)):
    fish[i] = int(fish[i])

def simulate_day(fish_list, day):
    for i in range(len(fish_list)):
        if fish_list[i] == 0:
            fish_list[i] = 6
            fish_list.append(8)
        else:
            fish_list[i] -= 1

    if day == 80:
        return fish_list
    else:
        return simulate_day(fish_list, day+1)

fish = simulate_day(fish, 1)
print(len(fish))