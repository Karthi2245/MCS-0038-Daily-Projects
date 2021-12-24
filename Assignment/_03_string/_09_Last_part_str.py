# P01. REQ : Last Part Of the String:

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
message = "Welcome to the world of python"
str1 = message.split()
print("The last part of the string is".ljust(40, '.'), ':', str1[-1])

print("-----2. Algorithm--------")
# 2. Algorithm
message = "Welcome to the world of python"
str1 = message.split()
print("The last part of the string is".ljust(40, '.'), ':', str1[-1])

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
# Python3 program to count words


def last_part(message):

    str1 = message.split()
    return str1


obj = last_part("Welcome to the world of Python")
print("The last part of the string is".ljust(40, '.'), ':', str1[-1])

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")

class LastPart:
    def last_part(self, message):
        str1 = message.split()
        return str1[-1]


obj1 = LastPart()
print(obj1.last_part('Welcome to my World'))
# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
