family =['Name: Jack', 'Jill','Janice','Adam']
handle = open("family.txt", "w")

for x in family:
    handle.write(x+ '\n')

handle.close()
