from ast import For
import math
import time


# ? Variables
# name ="sourin"
# print(type(name)) #?checking the type
# age ="10"
# print(age)
# print(age+name) #* not working,as i'm trying to mix int with string. needs to be typecasted
# print(str(age)+" "+name) #? Typecaste: both are string right now (string literal)
#! float

# height =233.5
# print("your height is "+str(height)+"cm") #? typecasting/ string literal while printing

#! boolean
# me=False #?not in quotes
# print(type(me))

#! multiple assignment
# multiple assignment=allows us to assign multiple variables at the same time in one line of code
# name="Bro"
# age = 21
# attractive=True
# print(name)
# print(age)
# print(attractive)
# * multiple assignment->The correct way
# name, age,attractive="Bro",21,True
# print(name)
# print(age)
# print(attractive)
# * another example
# sourin=anirban=addya=sil=20
# print(sourin)
# print(anirban)
# print(addya)
# print(sil)
#! Few String methods


# name1 = "Sourin"
# print(len(name1)) #?Length of string

# ? ******you cant start any python line with space*********

# print(name1.find("s")) #? find something in string, returns first-find one, case sensitive

# print(name1.capitalize())#?  only the first letter, makes rest letters small **************IMP*********

# print(name1.upper())#? all to upper case

# print(name1.lower())

# print(name1.isdigit()) #?check it is digit or not

# print(name1.isalpha()) #? true when string contains alphabet only

# print(name1.count("o")) #? count number of 'o' in the string

# print(name1.replace('o','i'))

# print(name1*3)


#!  TYPECASTING

x = 1  # int
# y=2.0 #float
# z="3" #string

# y=int(y) #? now y is an int
# print(y)

# print(z*3) #? //'333' : unlike js,,js would have converted it from string to number; but not here

# print(float(x)) #? x is now an float,,but only till this statement is printed, original data is unaltered

# x=float(x) #? now x is a float, main data altered in this case   ***********IMP with the above************
# print(type(x))

# y=str(y) #? to convert y into string, original data altered in this case  **********IMP***********
# print(y)
# print(type(y))

#* sometime we have to print some data, like string with integer data, yeh cheez tabhi kaam ayga, niche dekho


#! User input in python

# name=input("Enter your name: ") #? we have to store the input data further, better storing it in a variable: 'name'

# print("hello "+name)

# age=int(input("enter your age: ")) #? taking input in int type

# print("age is " + age) #? **********adding string with int is not possible in python*************


# print("age is " + str(age)) #? but this way it is posssible as int is converted to string


#! Math Functions
# ? have to import math at first lines

# pi=3.14
# print(round(pi))

# print(math.ceil(pi))

# print(math.floor(pi))

# print(abs(pi)) #?equivalent to modulus of physics |pi|, will give +ve value even if the input is -ve

# print(pow(3,2))

# print(math.sqrt(64))


# x=1
# y=2
# z=3

# # print(max(pi,x,y,z))
# print(min(pi,x,y,z))


#! String Sclicing: extracting elements

# *Slicing = create a substring by extracting elements from another string indexing[] or slice()
# *      [start:stop:step]


name = "Sourin Shelly"

# first_name=name[0:6] #or first_name=name[:6]
# last_name= name[7:13] #or last_name= name[7:]
# funky_name=name[0:6:2] #? it will print every second index

# print(funky_name)

# reverse1=name[::-1] #? way of reversing string with slice

# print(reverse1)

# website1="http://google.com"
# website2="http://wikipedia.com"

# slice1=slice(7,-4) #?? you can copy this over and over again, see below

# print(website1[slice1])
# print(website2[slice1])


#! Else If statement

# age = int(input("Enter your age: "))

# if age >= 18:
#     print("you are adult")
# elif age == 100:  # ? it wont execute, as first condition is satifying, so orders matter
#     print("you are a century old")
# elif age < 0:
#     print("Not born yet")
# else:
#     print("a child")


#!  Logical operators

# * and, or and not operators
# temp=int(input(" enter temp outside: "))

# if temp >=0 and temp <= 30:
#         print("the temp is good today")
#         print("go outside!")
# elif temp<0 or temp>30:
#         print("temp is bad")
#         print("stay home")


#! While Loops: wokls as long as conditions remain true

# * infinite loop
# while 1==1: #? as this condition will remain true forever
#         print("help! stuck in a loop!")

# name = ""  # ? **************IMP****************
# while (len(name)) == 0:
#     name = input("enter your name: ")
#     # ? this algo means it will run in infinite loop untill you enter name
# print("hello " + name)

# * Another way of above thing

# name1 = None
# while not name1:
#     name1 = input("enter your name: ")
# print("hello " + name1)


#! For loops:  a block of code execute for limited amopunt of timmes


# for i in range(10):
#         print(i+1)

# for i in range(50,100+1): #? starts from 50 and ends at 100
#         print(i)

# for i in range(50,100+1,2): #? start, end, condn of increasing
#         print(i)

# for i in "Sourin":
#         print(i)  #? prints each letter in every line


# for seconds in range(10,0,-1):
#         print(seconds)
#         time.sleep(1) #* have to import time in the begining
# print("HNY")
# #?without time.sleep method all the numbers will be printed alltogether, it prints after every 1 sec


#! NESTED Loops: loop inside loop


# row=int(input("Enter rows: "))
# col=int(input("Enter cols: "))
# symbol=input("Enter your symbol: ")

# for i in range(1,row):
#         for j in range(col):
#                 print(symbol, end="") #? by default print statement creates a new line, so with end"" it prints on the same line
#         print()


#! Break Continue
# break = used to terminate the loop entirely
# continue = skips to the next iteration of the loop
# pass = does nohing, acts as a placeholder

# while True: #? another process of unlimited loops
#         name = input("Enter your name: ")
#         if name != "":
#                 break


# phn_num = "123-456-789"
# for i in phn_num:
#     if i == "-":
#         continue #? it will ignore -
#     print(i, end="")

# * PASS
# for i in range(1, 20):
#     if i == 13:
#         pass
#     else:
#         print(i)


#! Lists= used to store multiple items in a single variable

food = ["piza", "Sauce", "apple"]
# print(food)
# print(food[1])


# food.append("pastry")

# food.remove("piza")

# food.pop() #? it removed the last element

# food.sort() #? alphabetically sorted

# food.clear() #? removes all the elements


# food.insert(1, "cake")
# for x in food:
#         print(x)

#!  2D list
