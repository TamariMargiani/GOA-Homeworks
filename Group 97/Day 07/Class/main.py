#  for loop - ვიყენებთ როდესაც ვიცით რამდენი იტერაციაა საჭირო.

#  while loop - როდესაც არ ვიცით რამდენი იტერაციაა საჭირო.

# for i in range(100):
#     print(i)

# for i in range(11):      # გამოიტანს 0-დან 10-ის ჩათვლით
#     print(i)

# for i in range(20, 10, -3):
#     print(i)

# for i in range(0, 50, 2):    #  ლუწი რიცხვების გამოტანა
#     print(i)

# for i in range(1, 50, 2):    # კენტი რიცხვების გამოტანა
#     print(i)

#  range()-ში გადავცემთ მხოლოდ რიცხვით მნიშვნელობას ანუ integer-ს


# name = 'Tamari'
# for char in name:
#     print(char)

# for char in 'Tamari':
#     print(char)


# name = input('Enter your name: ')
# for char in name:
#     print(char)


# while გამოიყენება იმისათვის, რომ გამოიტანოს კოდის ბლოკი იქამდე სანამ პირობა არის ჭეშმარიტი. 

# while True:  # ამ ფორმით დაწერილი while ციკლი დაბეჭდავს Hello-ს უსასრულოდ :))
    # print('Hello')

# ice_cream = 10
# while ice_cream > 0:
#     print('Ice-cream Sold!')
#     ice_cream = ice_cream - 1  >>>>  ice_cream -= 1
# print('All ice-cream sold!')


#   1. ice_cream = 10  >>>  10 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  10 - 1 = 9
#   2. ice_cream = 9  >>>  9 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  9 - 1 = 8
#   3. ice_cream = 8  >>>  8 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  8 - 1 = 7
#   4. ice_cream = 7  >>>  7 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  7 - 1 = 6
#   5. ice_cream = 6  >>>  6 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  6 - 1 = 5
#   6. ice_cream = 5  >>>  5 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  5 - 1 = 4
#   7. ice_cream = 4  >>>  4 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  4 - 1 = 3
#   8. ice_cream = 3  >>>  3 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  3 - 1 = 2
#   9. ice_cream = 2  >>>  2 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  2 - 1 = 1
#   10. ice_cream = 1  >>>  1 > 0 (True) >>>  დაიბეჭდება 'Ice-cream Sold'  >>>  1 - 1 = 0
#   11. ice_cream = 0 >>>  0 > 0 False - შეწყდება კოდი!!! რადგან პირობა აღარ არის ჭეშმარიტი


# num = 10
# num = num - 1 
# print(num)

# num = 12
# num = num + 2
# print(num)

# num = 5
# num += 10  
# print(num)


# num = 10

# num += 5
# num -= 2
# num *= 10
# num //= 5
# num **= 2
# num %= 5
# print(num)


# counter = 0
# while counter < 4:
#     print(counter)
#     counter = counter + 1

# i = 0
# while i < 5:
#     print(i)
#     i = i + 1



