# HOMEWORK

# 1. 

list = [47, 63, 16, 98, 32]

list.sort()
removed_num = list.pop(0)

print(removed_num)
print(list)



# 2. 

list = [10, 30, 20, 10, 50, 10]

x = list.count(10)
print(x)

if x > 2:
    list.remove(10)
print(list)



# 3.

nums = [20, 40, 60, 80]
print(nums)

nums.copy()
nums.append(100)
nums.reverse()
print(nums)



# 4. 

list = [-5, -10, 20, 40, 50]

list.sort()

print(list)

if list[0] < 0:
    list.clear()
    print(list)


# 5.

nums = [5, 3, 8, 6, 9, 1, 6]

nums.sort()
print(nums)

x = nums.count(9)
print(x)

nums.remove(9)
print(nums)



# 6. 

list = [89, 13, 456, 98, 54, 786]

print(list[0:3])


# 7. 

list = [45, 78, 98, 32, 25, 46, 31, 72]

print(list[4:])


# 8. 

list = [75, 24, 65, 12, 321, 46, 98]

print(list[2:5])