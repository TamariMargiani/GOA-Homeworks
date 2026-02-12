#  1. ასაკის სარკე

age = int(input('How old are you? :' ))
print(age >= 18)
print(type(age))


# 2. ორი რიცხვის დუელი

num1 = 12.3
num2 = 46.5

sum1 = num1 * num2
sum2 = num1 + num2

print(sum1 > sum2 )

print(sum1)
print(sum2)

print(type(sum1))
print(type(sum2))


# 3. სიმართლის თამაში

user1 = int(input('num1: '))
user2 = int(input('num2: '))

print(user1 > user2)
print(user1 > 0)
print(user2 > 0)


# 4. სახელისა და ასაკის კონტრაქტი

name = input("What's your name?: ")
age = int(input('How old are you?: '))

adult = age >= 21
print("User " + name + " is adult: " + str(adult))


# 5. კალკულატორი, რომელიც ფიქრობს

X = 110
Y = 20
Sum = X / Y
print(Sum)
print(type(Sum))


# 6. სიმაღლის გამოცანა

user = float(input("What's your height?: "))
print(int(user))
print(user > 1.75)


# 7. რიცხვის ხასიათი

X = 9
print(X > 0)
print(X < 0)
print(X == 0)


# 8. სტრინგი რიცხვის წინააღმდეგ

num = input('Z: ')
print(type(num))
print(int(num))
print(type(int(num)))
print(int(num) >= 100)

num = int(input('Z: '))
print(type(num))
print(num >= 100)


# 9. საშუალო არ არის უბრალოდ რიცხვი

X = 2.5
Y = 3.9
Z = 7.6
sum = 2.5 + 3.9 + 7.6 
print(sum // 3)

average = (2.5 + 3.9 + 7.6) // 3
print(average)
print(average > 50)
print(type(average))


# 10. ტიპების დეტექტივი

num = input('x: ')
print(int(num))
print(type(int(num)))
print(float(num))
print(type(float(num)))

num1 = float(input('y: '))
print(type(num1))
print(int(num1))
print(type(int(num1)))

# 11. Sololearn + 