# For loop - For ციკლი

# print('გილოცავ ვალენტინობის დღეს')
# print('გილოცავ ვალენტინობის დღეს')
# print('გილოცავ ვალენტინობის დღეს')


# ერთი და იგივე მრავალჯერ რომ არ დავბეჭდოთ სათითაოდ, უნდა გამოვიყენოთ For loop

# for i in range(100):
#     print('გილოცავ ვალენტინობის დღეს')  - დაიბეჭდება 100-ჯერ

# name = 'Tamari'
# სახელი = 'თამარი'
# print(სახელი)


# for i in range(3):
#     print(i)

# for i in range(5):
#     print('Hello')

#  Indentation - ინდენტაცია - კედლიდან დაშორება

# for i in range(5):
#     print('Congrats')

# for num in range(6):
#     print(num)

# for i in range(11):
#     print(i)

# for i in range(1, 15):
#     print(i)

# for i in range(5, 15, 2):
#     print(i)

#       N1 N2 N3
# range(5, 15, 2)

#  N1 - საიდან უნდა დაიწყოს ათვლა
#  N2 - სადამდე უნდა გაგრძელდეს ათვლა
#  N3 - ყოველ იტერაციაზე რამდენით უნდა გაიზარდოს

# for i in range(5, 100, 10):
#     print(i)
     
# for i in range(1, 10):
#     print(i * 2)

# i
# 1 === 1 * 2
# 2 === 2 * 2
# 3 === 3 * 2
# 4 === 4 * 2
# 5 === 5 * 2 და ა.შ. ცხრის ჩათვლით ანუ 10-მდე.

# for num in range(10, 1, -1):
#     print(num)

# For ციკლი სტრინგისთვის

# animal = 'tiger'
# for char in animal:
#     print(char)


# total = 3

# for i in range(100):
#     print(total * i)

#  While loop - while ციკლი

#  while ციკლი ამეორებს კოდს სანამ პირობა არის ჭეშმარიტი

# seats = 500
# while seats > 0:
#     print('Sell ticket')
#     seats = seats - 1

#  500 > 0 === true >>> 'ST' >>> 500 - 1 = 499
#  499 > 0 === true >>> 'ST' >>> 499 - 1 = 498
#  498 > 0 === true >>> 'ST' >>> 498 - 1 = 497 და ა.შ.


# while True:
#     print('AAAAAA') - ამ შემთხვევაში უსასრულოდ დაიბეჭდება "AAAAAA"


# counter = 0
# while counter < 4:
#     print(counter)
#     counter = counter + 1

# 0 < 4 === true >>> '0' >>> 0 + 1 = 1
# 1 < 4 === true >>> '1' >>> 1 + 1 = 2
# 2 < 4 === true >>> '2' >>> 2 + 1 = 3
# 3 < 4 === true >>> '3' >>> 3 + 1 = 4
# 4 < 4 === false  --- რაკი ეს პირობა მცდარია, კოდი შეწყდება და აღარაფერს აღარ დაბეჭდავს!


# კომპიტერი კითხულობს ბაინარი კოდს ანუ ნულებს და ერთებს. True  = 1  /  False = 0    (num != 0) - თუ ეს პირობა სწორია, მაშინ მისი მნიშვნელობა არის 1 და თუ ეს პირობა არ არის სწორი მაშინ მისი მნიშვნელობა არის 0. 

