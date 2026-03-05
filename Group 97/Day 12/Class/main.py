 # Classwork

# ფუნქცია - Functions - ფუნქციები არის ხელმეორედ გამოყენებადი კვების ბლოკი. 
# ფუნქცია არის კოდის ბლოკი, რომელიც გამოიყენება კონკრეტული დავალებებისთვის.

# def greet():
#     print('Hello')

# greet()


# def - ფუნქცია, def ქმნის ფუნქციას
# greet(): - ფუნქციის დასახელება
# () - პარამეტრის შესატანი ადგილი!!  - print('Hello') - ის რაც უნდა გამოიტანოს ეკრანზე, ფუნქციის გამოძახების შედეგად. 
# greet() - ფუნქციის გამოძახება (ფუნქციის დასახელებით ვიძახებთ ფუნქციას)


# def x():
#     print('This is x function')
#     print('When we call x function')
#     print('These prints will be displayed')

# x()   # ფუნქცია შეგვიძლია გამოვიძახოთ იმდენჯერ, რამდენჯერაც ჩვენ გვინდა.


# def new_func():
#     x = 10
#     y = 20
#     z = x + y
#     print(z)
#     print(z ** y)
#     print(z // y * x)

# new_func()

# გვაქვს ორი ტიპის ცვლადი - გლობალური ცვლადი(global variable) და ლოკალური ცვლადი(local variable)

# ზოგადი ცვლადი არის ისეთი ცვლადი, რომელიც ჩვენ შეგვიძლია გამოვიყენოთ ბევრ რამეში და ჩვენ შეგვიძლია მივწვდეთ მას ნებისმიერი ადგილიდან. 
# ზოგადია ცვლადი, რომელიც არც ფუნქციაშია შექმნილი, არც for ან while ციკლებში, არც პირობით განცხადებებში და ა.შ. 

# ლოკალურია ცვლადი, რომელიც იქმნება რაღაცის შიგნით. მაგ. ფუნქციის შიგნით, პირობითი განცხადების შიგნით, for ციკლის შიგნით და ა.შ.


# def greet(name):  # (name) არის პარამეტრი, ანუ რასაც ვწერთ ფუნქციის დასახელების ფრჩხილებში არის პარამეტრი. # greet ფუნქციის შიგნით შევიტანეთ name პარამეტრი
#     print('Hello', name)

# greet('Tamari')  # რასაც ვწერთ გამოძახების შიგნით ანუ ამ შემთხვევაში 'Tamari',  ეწოდება არგუმენტი.


# პარამეტრის დანიშნულებაა მომხმარებლის მიერ შემოტანილი მნიშვნელობა ჩაწეროს სადმე.

# def sum(x, y):
#     print(x + y)
#     print(x // y)
#     print(x * y)
#     print(x * x)

# sum(10, 5)


# def greet(name='User'):
#     print('Hello', name)

# greet()
# greet('Beka')
# greet('Davit')
# greet('Tamari')


# f სტრინგი ან f ფორმატირება 
    # print(f"Hello {name}")



# def greet(name):
#     print(f"Hello {name}")

# user_name = input('Enter your name: ')      # name = input('Enter your name: ')
# greet(user_name)                            # greet(name)


# def greet(name, last_name):
#     print(f'Hello {name} {last_name}')

# greet(input('Enter your name: '), input('Enter your last name: '))


# def info(name, surname, age, profession, experience):
#     print(f'I am {name} {surname}, I am {age} years old, I used to be a {profession} for {experience} years, but now I am a student at GOA')

# info(input('Enter your name: '), 
#      input('Enter your surname: '), 
#      input('Enter your age: '),
#      input('Enter your profession: '),
#      input('Enter your experience: '))


# def distance(km):
#     print(km * 1000)
#     print(km * 100000)

# distance(int(input('Enter km: ')))
