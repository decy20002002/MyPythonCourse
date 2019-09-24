import sys
import math
price1 = float(input("What is the price of product 1? "))
discount1 = int(input("Produc 1 discount? "))

price2 = float(input("What is the price of product 2? "))
discount2 = int(input("Produc 2 discount? "))

product1_final_price = price1 - (price1 * discount1 / 100)
product2_final_price = price2 - (price2 * discount2 / 100)

# print('Price per ounce of product 1:')
# print(price_per_ounce1)
# print('Price per ounce of product 2:')
# print(price_per_ounce2)
# print(price_per_ounce1 < price_per_ounce2)

print('Original Price of Product 1:' , price1)
print('New Price of Product 1 after ' + str(discount1) + ' % discount:' , product1_final_price)
print('Original Price of Product 2:' , price2)
print('New Price of Product 2 after ' + str(discount2) + ' % discount:' , product2_final_price)

# input()
