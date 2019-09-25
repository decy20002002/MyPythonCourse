
counter = 0
limit = input('Please set the limit: ')
while True:
    if limit == False:
        counter = 4
    if counter == int(limit):
        break
    if (counter %2 != 0):
        print(counter, end=" ")
    counter+=1
print('\n', 'Finished looping')