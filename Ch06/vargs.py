
def slice_list(list_to_slice, *upper_bounds):
    """Returns slice of list if uppper bound is valid"""

    list_to_return = []

    for upper_bound in upper_bounds:
        if(len(list_to_slice)>upper_bound):
            print('Slicing...')
            list_to_return.append(list_to_slice[:upper_bound])
        else:
            list_to_return.append(None)
        
    return list_to_return

some_nums = [2,6,4,2,22,54,12,8,-1]

print(slice_list(some_nums, 12,7,2,3))
