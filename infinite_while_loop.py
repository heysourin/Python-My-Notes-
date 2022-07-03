while (len(name)) == 0:
    name = input("enter your name: ")
    #it will keep on asking your name if you submit it blank
print("hello " + name)

# another way to do the same

name1 = None
while not name1:
    name1 = input("enter your name: ")
print("hello " + name1)

