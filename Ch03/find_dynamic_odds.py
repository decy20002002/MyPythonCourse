
counter = 0
limit = input('Please set the limit: ')
while True:
    if counter == 20:
        break
    if (counter %2 != 0):
        print(counter, end=" ")
    counter+=1
print('\n', 'Finished looping')