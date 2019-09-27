some_nums = [2,6,4,2,22,54,12,8,-1]

print('The some_nums list is ',len(some_nums), ' long')
print('the sum of the list is: ',sum(some_nums))

third_item = some_nums[2]

print('The third item is ', third_item)

highest_num = some_nums[0]

for x in some_nums:
    if x > highest_num:
        highest_num = x

print('The highest number is ', highest_num )

for x in range(len(some_nums) - 1):
    print(x)
    if (x%2==0):
        some_nums[x] = 11

print(some_nums)
