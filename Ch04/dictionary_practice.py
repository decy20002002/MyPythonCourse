
squares = {1:1, 5:25, 2:4, 3:9, 4:16}
print('squares = ', squares)

for key, value in squares.items():
    print(f"The square of {key} is {value}")

# pop() removes output value
print('Remove key(4) = ', squares.pop(4))
print('squares = ', squares)

#add item into dictionary
squares[6] = 36
print('squares added new value [6]: ', squares)
print('squares = ', squares)

#using popitem() removes the last added item
print('square.popitem() returns ', squares.popitem())
print('squares after popitem', squares)

#delete an item using bracket notation
del squares[1]
print('squares after del squares[1]',squares)

#del squares[7] = KeyError: 7

#remove all items
squares.clear()
print('squares after squares.clear()', squares)


for x in range(1,11):
    #if x == 0:
    #    continue
    #else:
        y = x*3
        #print(x,y)
        squares[x] = y
        print(squares)

print(f'final squares after inserted is: ',squares)

    