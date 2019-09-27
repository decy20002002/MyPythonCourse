print(8,bin(8))
print(11,bin(11))

print(6,bin(6))
print(7,bin(7))


binary_five_string = bin(5)  

#specified as binary, but int
binary_five  = 0b101; 
binary_three = 0b011;

#do not need leading zeroes
binary_two = 0b11;

print(binary_five)
print(binary_three)
print('binary_five is ',type(binary_five))

print('OR\t',bin(binary_five | binary_three))
print('AND\t',format(binary_five & binary_three,'#05b'))
print('XOR\t',bin(binary_five ^ binary_three))


print(6,bin(6))
print(7,bin(7))

print('OR\t',bin(6 | 7))
print('AND\t',bin(6 & 7))
print('XOR\t',bin(6 ^ 7))
print('XOR\t',format(6 ^ 7,'#05b'))
