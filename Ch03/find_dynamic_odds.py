x = 0
counter = 0
limit = input('Please set the limit: ')

if limit == "":
    limit = 4
else:
    limit = int(limit)

while counter < limit:
    #if (counter %2 != 0):
    print(counter, end=" ")
    counter+=1
    # print(counter)
# print('\n', 'Finished looping')

