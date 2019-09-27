import random

num_set = {2,6,4,2,22,54,12,8,-1}

print(num_set)
print(len(num_set))


name_list=['Adam','Barry','Doug','Cathy','Ellen']

volunteers =set(random.sample(name_list,3))
qualified =set(random.sample(name_list,3))

print('volunteers are:',volunteers)
print('qualified are:',qualified)

new_team = volunteers.intersection(qualified)
print('new team',new_team)

vowels = {'a','e','i','o','u'}
words = ['alligator','penguin','water fowl','giraffe']

for word in words:
    counter = 0
    for letter in word:
        if letter in vowels:
            counter += 1
    print(f'the word {word} has {counter} vowels')

