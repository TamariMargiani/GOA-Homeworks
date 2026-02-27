# list - გამოიყენება იმისათვის, რომ ჩვენ შიგნით შევინახოთ მნიშვნელობები. მასში ჩვენ შეგვიძლია შევიტანოთ ნებისმიერი მონაცემთა ტიპის მნიშვნელობა.

# len ფუნქცია - Lis Length - გვეხმარება განვსაზღვროთ/დავთვალოთ რამდენი მნიშვნელობაა შეტანილი სიაში.

# list = [10, 20, 30, 40, 50, True, False, 'Fruit']

# print(len(list))

# print(type(list))

# print(list[1])

# chars = ['A', 'B', 'C']
# print(chars[2])
# print(len(chars))


# უარყოფითი ინდექსინგი 

# fruit = ['banana', 'apple', 'strawbarry', 'peach', 'kiwi', 'mango']
# print(fruit[-1])
# print(fruit[0:3])
# print(fruit[1:4])

# print(fruit[:5])
# print(fruit[0:])

# print(fruit[-4:-1])
# print(fruit[2:5])
# print(fruit[-5:])
# print(fruit[-6:3])


#  #  #  #  #

# list = ['apple', 'banana', 'cherry']

# if 'cherry' in list:
#     print('Yes, "cherry" is in the list')
# else:
#     print("No, 'cherry' isn't in the list")

# for x in list:
    # print(x)


# სიაში მნიშვნელობების შეცვლა

# thislist = [30, 40, 60, 70]
# thislist[1] = [80]   # thislist[1] = 80
# print(thislist)

# list = ['apple', 'banana', 'cherry']

# list[0] = ['watermelon']
# print(list)

# list[1:3] = 'melon', 'pear'
# print(list)


# for ციკლი სიებისთვის

# list = ['apple', 'banana', 'cherry']

# for i in list:                    # i-ს ნაცვლად ნებისმიერი ასო/დასახელება შეგვიძლია დავწეროთ
#     print(i + ' I have this fruit')     

# for x in list:
#     print(str(1) + ' ' + x)


# list = ['apple', 'banana', 'cherry']

# for i in range(len(list)):  # იგივეა რაც for i in range(3)  - ამ კონკრეტულ კოდში len ეუბნება range-ს კონკრეტულად რამდენი მნიშვნელობისგან შედგება list-ი.
#     print(list[i])
# print(len(list))


# list = ['apple', 'banana', 'cherry']
# print(list)
# print(len(list))



# list = ['apple', 'banana', 'cherry']

# i = 0
# while i < len(list):
#     print(list[i])   # print(len(list))
#     i = i + 1    # i += 1
# print(len(list))




  # .append() - ამატებს სიაში(სიის ბოლოს) ახალ მნიშვნელობას

# nums = [20, 30, 50, 60]

# nums.append(90)

# print(nums)


# nums = [20, 30, 50, 60]

# for i in nums:
#     if len(nums) < 5:
#         nums.append(80)
# print(nums)


# nums = [20, 30, 50, 60]

# nums.append('Hello World')

# print(nums)


# nums = [20, 60, 50, 90]

# strings = ['a', 'b', 'c']

# nums.append(strings)

# print(nums)



# .clear() - სიიდან ამოშლის ყველა მნიშვნელობას

# x = [20, 30, 50, 60]

# for i in x:
#     if len(x) > 2:
#          x.clear()
# print(x)
         

# print(nums)

# nums.clear()

# print(nums)



# .copy() - აკეთებს სიის ასლს 

# nums = [20, 30, 50, 60]
# x = nums.copy()
# print(x)

# if nums == x:
#     print('List is copied')



# .count - ითვლის რამდენჯერაა მოცემული ერთი და იგივე მნიშვნელობა სიაში

# nums = [60, 20, 60, 50, 60, 90, 60]

# x = nums.count(60)
# print(x)


# .remove() - სიიდან ამოშლის კონკრეტულ მნიშვნელობას

# fruits = ['apple', 'cherry', 'kiwi']

# fruits.remove('kiwi')
# fruits.remove('apple')

# print(fruits)


# fruits = ['apple', 'cherry', 'kiwi']

# if 'cherry' in fruits:
#     print('There is "cherry" in the list, so we remove it.')
#     fruits.remove('cherry')
#     print(fruits)
# else:
#     print('There is no "cherry" in the list.')
#     print(fruits)


# .pop() - სიიდან ამოშლის მნიშვნელობას, ოღონდ ინდექსის მითითებით

# booleans = [True, False, 13]

# booleans.pop(2)
# print(booleans)

# შეგვიძლია ტერმინალზე გამოვიტანოთ ამოშლილი მნიშვნელობა

# booleans = [True, False, 13]

# removed_item = booleans.pop(1)
# print(removed_item)


# .reverse() - შემოაბრუნებს მთლიან სიას

# nums = [20, 60, 50, 90, 40, 10, 80, 70, 30, 100]

# nums.reverse()
# print(nums)



# .sort - ალაგებს სიაში არსებულ მნიშვნელობებს ზრდადობით ან კლებადობით

# nums = [20, 60, 50, 90, 40, 10, 80, 70, 30, 100]

# nums.sort()
# print(nums)

# nums.sort(reverse=True)
# print(nums)