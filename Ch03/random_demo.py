import random

list = []

for x in range(3):
    list.append(input('Enter name: '))
    #list = ['Abe', 'Cathy', 'Bod']

print(list)
print('selected: ', random.choice(list))
print('sampling: ', random.sample(list,2))
