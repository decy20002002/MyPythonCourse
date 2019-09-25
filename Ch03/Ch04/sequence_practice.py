numbers = [9,3,1,39,90,120,-5,20,11]
print('The lowest number in Min is: ', min(numbers))

#OR

lowest_num = numbers[0]

for x in numbers:
    if x < lowest_num:
        lowest_num = x
print('The lowest number in for next loop is ', lowest_num)
