import sys

filename = sys.argv[1]

nums = []
with open(filename, 'r') as file:
    for line in file:
        nums.append(int(line.strip()))
nums.sort()
a = nums[len(nums) // 2]

count = 0
for num in nums:
    while num != a:
        if num < a:
            num += 1
            count += 1
        elif num > a:
            num -= 1
            count += 1

print(count)

