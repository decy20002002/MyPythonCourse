x = 0
counter = 0
limit = input('Please set the limit: ')

if limit == "":
    counter = 4
else:
    counter == int(limit)

while x < counter:
    # if (counter %2 != 0):
    #    print(counter, end=" ")
x+=1
print(x)
# print('\n', 'Finished looping')