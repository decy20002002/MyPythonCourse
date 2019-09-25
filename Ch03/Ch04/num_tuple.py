some_nums = (2,6,4,2,22,54,12,8,-1)
#some_nums = [11,11,11,11,11,54,11,11,11]
#for x in range(9):
#    some_nums.append(input('Enter numbers: '))

print(len(some_nums))
print(min(some_nums))
print(max(some_nums))
print('the sum of the list is: ', sum(some_nums))
#print('the third item on the list is: ', some_nums[2])

highest_num = some_nums[0]

for x in some_nums:
    if x > highest_num:
        highest_num = x
print('The highest number is ', highest_num)

for x in range(len(some_nums) - 1):
    print(x)
    print(some_nums)
    if (x%2==0):
        some_nums[x] = 100
print(some_nums)
