
def change_fist_value(list_to_change):
    '''Changes a list inside the function'''

    list_to_change[0]='something different'

some_nums = [2,6,4,2,22,54,12,8,-1]
print(some_nums)
change_fist_value(some_nums)
print(some_nums)