# HOMEWORK

# 1. 

list = []

x = int(input('Enter number: '))
y = int(input('Enter number: '))
z = int(input('Enter number: '))

list.append(x)
list.append(y)
list.append(z)

print(list)



# 2. 

list = [20, 40, 50, 80]

print(list)

list.clear()

print(list)



# 3. 

list = ['apple', 'banana', 'cherry', 'kiwi', 'mango']
print(list)

list.copy()
list[0] = 'peach'
print(list)



# 4.

nums = [2, 5, 8, 9, 5, 8, 3, 5, 6, 5]

x = nums.count(5)
print(x)



# 5. 

new_list = [132, 15, 58, 9, 97, 88, 12, 6]

removed_num = new_list.pop(7)
print(removed_num)
print(new_list)



# 6. 

list = [2, 8, 9, 5, 8, 3, 6]

list.remove(5)
print(list)



# 7. 

new_list = [132, 15, 58, 9, 97, 88, 12, 6]

new_list.reverse()
print(new_list)



# 8. 

new_list = [132, 15, 58, 9, 97, 88, 12, 6]

new_list.sort()
print(new_list)



# 9. 

list = []

num1 = int(input('Enter number: '))
num2 = int(input('Enter number: '))
num3 = int(input('Enter number: '))
num4 = int(input('Enter number: '))
num5 = int(input('Enter number: '))

list.append(num1)
list.append(num2)
list.append(num3)
list.append(num4)
list.append(num5)

list.sort()
list.pop(4)
print(list)



# 10.

list = [7, 9, 5, 3, 1, 5]

x = list.count(5)
print(x)

if 5 in list:
    list.remove(5)
    print(list)



# 11. 

list = [45, 80, 75, 55, 25]
print(list)

list.copy()
list.reverse()
print(list)



# 12. 

list = [50, 30, 10, 40]

total = 0

for i in list:
     total += i

if total > 100:
    list.clear()
    print(list)
else:
    print(list)    



# 13. 

list = [46, 78, 32, 49, 61]

list.sort()
list.remove(78)

print(list)


# 14.  W3schools +