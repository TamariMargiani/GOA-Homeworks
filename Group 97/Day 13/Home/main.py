# HOMEWORK

# 1. 

def sum(num):

 total = 0

 for i in range(1, num + 1):
    total += i

 return total             

print(sum(int(input('Enter number: '))))            




def sum():
  
  total = 0
  n = int(input('Enter number: '))

  for i in range(1, n + 1):
    total += i

  print(total)

sum()



# 2. 

def odd_num():

    num = int(input('Enter number: '))

    for num in range(1, num + 1):
          if num % 2 != 0:
           print(num)

odd_num()



def odd_count():

    num = int(input(('Enter number: ')))
    count = 0

    for num in range(1, num + 1):
          if num % 2 != 0:
           count += 1
    return count 

print(odd_count())



# 3. 


def sum():

    total = 0
    num = int(input('Enter number: '))

    while num != 0:
        total += num
        num = int(input('Enter number: '))

    return total
    
print(sum())



# 4. 

def sum(list):

    total = 0

    for num in list:
        total += num
    
    return total

print(sum([5, 7, 8, 9, 10, 22, 25]))



# 5. 

def even_nums(list):

    for nums in list:
        if nums % 2 == 0:
            print(nums)
        
even_nums([1, 5, 3, 6, 8, 20, 54])      # return ვერ გამოვიყენე ამ ფუნქციში



# 6. 


def list():

    new_list = [5, 10, 34, 5, 89, 54, 5, 23, 67, 5, 78, 34, 5]

    x = new_list.count(5)

    return x

print(list())

    

# 7. 

def num():

    x = 5

    return 5 * 5 * 5

print(num())             



def num(x):

    return x ** 3

print(num(int(input('Enter X: '))))



# 8. 

def nums():

    x = int(input('Enter x: '))
    y = int(input('Enter y: '))
    
    if x < y:
        return x
    else:
        return y

print(nums())



def nums (x, y):
     if x < y:
          return x
     else: 
          return y

print(nums(45, 65))




