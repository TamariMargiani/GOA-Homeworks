# HOMEWORK

# 1. 


def num(x):
   print(x ** 2)

num(5)


def num():
   x = 10
   print(x ** 2)

num()


def num():
   x = int(input('Number: '))
   print(x ** 2)

num()



# 2. 

def avarage(x, y, z):
    print((x + y + z) // 3)

avarage(10, 20, 30)


# 3. 

def num(x):
    if x > 0:
        print(True)
    else:
        print(False)
num(5)
num(-10)
num(int(input('Enter number: ')))



# 4. 

def num(x):
    print(x * 2)

num(65)
num(int(input('Enter number: ')))


# 5.

def sum(x, y=10):
    print(x + y)

sum(15, 30)
sum(45)


# 6. 

def greet(name ='Guest'):
    print(f'Hello {name}')

greet()
greet('Tamari')


# 7. 

def sum(x, y):
       print(x + y)

sum(int(input('X: ')), int(input('Y: ')))


# 8. 

def age():
    age = int(input('Enter your age: '))
    print(age + 10)

age()


# 9. 

def user(name):
    print(f'Hello {name}')

user(input('Enter your name: '))



def user(name):
    return 'Hello ' + name

print(user(input('Enter your name: ')))




def user():
    user = input('Enter your name: ')
    return 'Hello ' + user

print(user())



# 10. 

def product():
    x = int(input('Enter X: '))
    y = int(input('Enter Y: '))
    z = int(input('Enter Z: '))
    return x * y * z            # print(x * y * z)

print(product())                # product()



# 11. 

def temp():
    C = float(input('Enter temperature: '))
    F =  C * 9/5 + 32
    print(f'{C} ცელსიუს გრადუსი არის {F} ფარენჰეიტი.')

temp()



# 12.

def time():
    hours = int(input('Enter hour: '))
    minuts = hours * 60
    seconds = hours * 3600
    print(f'{hours} საათი არის {minuts} წუთი და {seconds} წამი.')

time()



# 13.

def scores(a, b, c, d):
    print((a + b + c + d) // 4)

scores(int(input('Enter score a: ')), 
       int(input('Enter score b: ')), 
       int(input('Enter score c: ')), 
       int(input('Enter score d: ')))
