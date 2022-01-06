f = open("input", "r")
nums = []
nums = f.read().replace("\n", "").split(",")
for i in range(len(nums)):
    nums[i] = int(nums[i])
    
diffs = []
for i in range(len(nums)):
    diff = 0
    find_num = nums[i]
    for num in nums:
        diff += abs(find_num - num)
    diffs.append(diff)

print(min(diffs))