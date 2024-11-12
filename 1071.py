nums = [int(input()), int(input())]
nums.sort()
sum = 0
for number in range(nums[0] + 1, nums[1]):
    if number % 2 != 0:
        sum += number
print(sum)