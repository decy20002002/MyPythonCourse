import random

num_set = {2,6,4,2,22,54,12,8,-1}

print(num_set)
print(len(num_set))

name_list = ['Adam','Barry','Doug','Cathy','Ellen']

volunteers = set(random.sample(name_list,3))
qualified = set(random.sample(name_list,3))

print('volunteers are: ', volunteers)
print('qualified are: ', qualified)

new_team = volunteers.intersection(qualified)
print('Qualified volunteers are: ', new_team)