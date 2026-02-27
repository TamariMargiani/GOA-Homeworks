
# HOMEWORK

# 1.  

# list_val = ['Tbilisi', 'Kutaisi', 'Telavi', 'Batumi', 'Zugdidi']
# print(list_val)


# # 2. 

# list_val = ['Tbilisi', 'Kutaisi', 'Telavi', 'Batumi', 'Zugdidi', 'Mestia', 'Kvareli', 'Tskaltubo', 'Rustavi', 'Kobuleti']
# print(list_val) 

# list_val[0] = 'Kartli'
# list_val[1] = 'Imereti'
# list_val[2] = 'Kakheti'
# list_val[3] = 'Adjara'
# list_val[4] = 'Samegrelo'
# print(list_val)


# # 3. 

# list_val = [5, 10, 30, 45, 95, 90, 25, 52, 78, 205]

# sum = list_val[0] + list_val[1] + list_val[2] + list_val[3] + list_val[4] + list_val[5] + list_val[6] + list_val[7] + list_val[8] + list_val[9] 
# print(sum)

# # 4.

# num1 = int(input('Enter number: '))
# num2 = int(input('Enter number: '))
# num3 = int(input('Enter number: '))
# num4 = int(input('Enter number: '))
# num5 = int(input('Enter number: '))

# # list_val = [num1 + 1 , num2 + 1, num3 + 1, num4 + 1, num5 + 1]

# list_val = [num1, num2, num3, num4, num5]

# for i in list_val:
#      print(i + 1)



# # 5. 

# list_val = [65, 30, 20, 15, 95]

# for i in list_val:
#     print(i + 1)



# 6. 

# list = [20, 21, 65, 11, 17, 84, 94, 35]

# odd_count = 0

# for i in range(len(list)):
#     if list[i] % 2 != 0:
#          print(list[i])
#          odd_count += 1
# print(odd_count)


    #  21 % 2 --- ნაშთი = 1 არ უდრის 0-ს ანუ  1 != 0 ამიტომ დაიბეჭდება 21 და შესრულდება მოქმედება  - odd_count += 1 რაც ნიშნავს, რომ 0 + 1 = 1
    #  65 % 2 --- ნაშთი = 1 არ უდრის 0-ს ანუ  1 != 0 ამიტომ დაიბეჭდება 65 და შესრულდება მოქმედება 1 + 1 = 2
    #  11 % 2 --- ნაშთი = 1 არ უდრის 0-ს ანუ  1 != 0 ამიტომ დაიბეჭდება 11 და შესრულდება მოქმედება 2 + 1 = 3
    #  17 % 2 --- ნაშთი = 1 არ უდრის 0-ს ანუ  1 != 0 ამიტომ დაიბეჭდება 17 და შესრულდება მოქმედება 3 + 1 = 4
    #  35 % 2 --- ნაშთი = 1 არ უდრის 0-ს ანუ  1 != 0 ამიტომ დაიბეჭდება 35 და შესრულდება მოქმედება 4 + 1 = 5
    

# list = [20, 25, 45, 23, 85, 24, 76, 13, 19, 56]

# odd_count = 0 

# for nums in list:
#     if nums % 2 != 0:
#         print(nums)
#         odd_count += 1
# print(odd_count)