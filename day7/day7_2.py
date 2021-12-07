f = open("input", "r")
nums = []
nums = f.read().replace("\n", "").split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])

diffs = []
for i in range(max(nums)):
    diff = 0
    find_num = i
    for num in nums:
        diff += sum(range(abs(find_num - num))) + abs(find_num - num)
    diffs.append(diff)

print(diffs)
print(min(diffs))