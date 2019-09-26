
def print_stars(count=10):
    print("*"*count)

print_stars()
print_stars(20)


def slice_list(list_to_slice, upper_bound):
    """Returns slice of list if uppper bound is valid"""
    if(len(list_to_slice)>upper_bound):
        print('Slicing...')
        return list_to_slice[:upper_bound]
    else:
        print('Value too high...',upper_bound)
        return None

some_nums = [2,6,4,2,22,54,12,8,-1]

print('Value returned',slice_list(some_nums,4))
print('Value returned',slice_list(some_nums,12))
