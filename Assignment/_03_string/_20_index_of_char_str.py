
# P01. REQ : Print the Index of a string character:

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)
'''

# Take the string
# Remove the odd position of the string
# Write the New string in White paper
# 1.Builtin functions

print("-----1. Built Functions--------")
name = "Karthikeyan"
for i in name:
    print(i, name.index(i))

# 2. Algorithm
print("-----2. Algorithm--------")

name = input("Enter a name :")

for i in range(len(name)):

    print(name[i], i)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def index_char():
    name = input("Enter a name :")

    for i in range(len(name)):
        print(name[i], i)


obj = index_char()

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")


log = 5
x = log / 10
print(x)