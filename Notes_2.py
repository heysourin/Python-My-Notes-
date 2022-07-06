#  #!2D list
# drinks=["water","sprite","frooti"]
# dinner=["pizza","burger","salad"]
# dessert=["cake", "misti"]

# food=[drinks,dinner,dessert]

# print(food)
# print(food[0]) #['water', 'sprite', 'frooti']
# print(food[0][1]) # sprite


#! TUPLE = collection which is ordered and unchangeable,
#!          used to group together related data

# student= ("Dude",21,"male")

# print(student.count(21)) #1 
# #***count() function counts how many times the "Dude" value appeares in the tuple


# print(student.index("male")) #2

# for i in student:
#     print (i)


# if "Dude" in student:
#     print("Bro is here")

#! SETS: collection which is unordered, unindexed. No duplicate values

# utensils={"fork","spoon","knife"}
# dishes={"bowls","plates","cup","knife"}

# print(utensils.difference(dishes)) #?it will print the uncommon things which
#                                 #? is not present in dishes


# print(dishes.difference(utensils))

# print(utensils.intersection(dishes ))


# utensils.add("plate")
# utensils.remove("fork")
# utensils.clear()

# utensils.update(dishes) #*they will be added in random order
# dishes.update(utensils) #*they will be added in random order

# dinner_table=utensils.union(dishes)
# print(dinner_table)

# for z in dinner_table:
#     print(z)

# for x in utensils:
#     print (x)

# print() #??To add new line

# for y in dishes:
#     print (y)


#! DICTIONARY = a changeable, unordered collection of unique key:
#!              value pairs Fast because they use hashing, allow us to
#!              access a value quickly, which, unlike other data types
#!              that hold only a single value as an element
#!              Dictionary holds key:value pair.


# capitals = {'USA': 'WashDC',
#             "India": 'New Delhi',
#             'China': 'Beijing',
#             "Russia": "Moscow"}

# print(capitals['Russia'])
# print(capitals['India'])
# print(capitals.get('Germany')) #?NONE
# print(capitals.keys()) #? prints the keys only
# print(capitals.values()) #? prints the values only
# print(capitals.items()) #? prints both

# capitals.update({'Japan':'Tokyo'}) #? Updating the list
# capitals.update({'USA':'Washington DC'}) #? Updating the list

# # #?Printing using for loop
# for keys, values in capitals.items():
#     print(keys,values)
# 
# print()
# #* Another way of doing the above thing
# for x, y in capitals.items():
#     print(y,x)


#! INDEXING/ Index Operator []: gives access to a sequence's element
#!                              like str,list,tuples

# name= "bro Code!"
# if(name[0].islower()):
#     name=name.capitalize()
#     print(name)


# last_namr=name[start_index:end_index]
# last_namr=name[4:8]
# fist_namr1=name[0:3].upper()
# print(last_namr)
# print(fist_namr1) 

# last_name=name[4:]
# print(last_name)

# last_char=name[-1]  #prints the last character
# print(last_char)

#! Functions

#? ****************IMP*************
# first_name=input("enter your first name: ")
# last_name=input("enter your last name: ")
# 
# def hello(_fstnm, _lstnm):
    # print( "Hello "+_fstnm+" "+_lstnm)
# 
# hello(first_name, last_name)
# 

#! Return Statement: functions send python values/objects back to thhe
#!                  caller. These values/objects are known as return statement

#? the above function with return satement
# first_name=input("enter your first name: ")
# last_name=input("enter your last name: ")

# def hello(_fstnm, _lstnm):
#     return ( "Hello "+_fstnm+" "+_lstnm)

# print(hello(first_name, last_name))

#?Another program with return statement
# name=input("Name: ")
# age=input("Age: ")

# def nameAge(nm,ag):
#     return ("Hello "+ nm+' of age '+ ag)

# print(nameAge(name,age))


#! Keyword Arguments: arguments preceded by an identifier whem we pass them to a function.
#!                    The order of the arguments doesnot matter,unlike 'positional arguments'
#!                    python knows the names of the arguments that our function receives

#? Positional arguments

# def hello(first,middle,last):
#     print("hello "+first+" "+middle+" "+last)

# hello("Sourin","Denver","Shelly")
# hello("Denver","Shelly","Sourin")
# hello(last="Shelly", middle="Denver",first="Sourin")

#! Nested function calls: function calls inside other function calls
#!                         innermost function calls are resolved first
#!                         returned value is used as argument for the next outer function

# num=input("Enter a positive num: ")
# num=float(num)
# num=abs(num) #? absolute value
# num=round(num)
#?or if you write it in a single line
# print(round (abs (float (input ("Enter a whole posi tive number: ")))))


#!Scope: the region that a variable is recognised.
#!        A variable is only availble from inside the region it is created
#!        A global and locally scoped versions of a variable can be created 



# name="Bro" #?Global scope(avilable inside and outside function)
# def display_name():
#     name="Code"#? local scoper(avialable only inside function)
#     print(name)

# print(name) #it will use global variable
# display_name() #if incase local variable is muted or not available it will use globaal variable


#? Pythons order of variables L=Local
#?                            E=Enclosed
#?                            G=Global
#?                            B=Built-in
