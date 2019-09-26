
vowels = {'a','e','i','o','u'}
words = ['alligator','penguin','water fowl','giraffe']

for word in words:
    counter = 0
    for letter in word:
        if letter in vowels:
            counter += 1
    print(f'the word {word} has {counter} vowels')
