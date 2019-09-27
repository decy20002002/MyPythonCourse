def capitalize_list(words):
    for i in range(len(words)):
        words[i] = words[i].capitalize() 
        print(words[i])

fruits = ['apple','cherry','banana']
print(fruits)
capitalize_list(fruits)
print(fruits)
