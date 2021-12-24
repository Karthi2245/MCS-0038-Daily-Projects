# P01. REQ : Count the character of the string:

'''
Topics:
--------
Operators
DM vs Loops    # DM = Decision making
Data structure
'''

# 0. Mathematics
'''
# Implement the solutions in white paper
# write the characters vertically on the white paper
# Note down the count of each character. '''

# 1.Builtin functions

# Python program to demonstrate
# string slicing

# String slicing
String ='ASTRING'

# Using slice constructor
s1 = slice(3)
s2 = slice(1, 5, 2)
s3 = slice(-1, -12, -2)

print("String slicing")
print(String[s1])
print(String[s2])
print(String[s3])

# 2. Algorithm

print("--------2. Algorithm----------")
name = "Karthikeyan"
str1 = name[:3]
str2 = name[2:6]
str3 = name[1:2:9]
str4 = name[1:3:10]
str5 = name[-6:-1]
str6 = name[:5]
str7 = name[1:]
str8 = name[-2:]

print("The Slicing of given string".ljust(40, "."), ':', str1)
print("The Slicing of given string".ljust(40, "."), ':', str2)
print("The Slicing of given string".ljust(40, "."), ':', str3)
print("The Slicing of given string".ljust(40, "."), ':', str4)
print("The Slicing of given string".ljust(40, "."), ':', str5)
print("The Slicing of given string".ljust(40, "."), ':', str6)
print("The Slicing of given string".ljust(40, "."), ':', str7)
print("The Slicing of given string".ljust(40, "."), ':', str8)




# Functions:
def slicingchar(str1):

    for char in str1[0:6]:
        print(char)
x = slicingchar("karthikeyan")

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
class Slicing:
    def slicingchar(self, str1):
        for char in str1[0:6]:
            print(char)


obj = Slicing()  # Object Creation
obj.slicingchar('Karthikeyan')

# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")

