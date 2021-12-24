# P01. REQ : Remove leading zero of given string :

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
print("-----1. Builtin Functions--------")


# 2. Algorithm:
print("-----1. Algorithm--------")
import re
ip = "216.08.094.196"
string = re.sub('\.[0]*', '.', ip)
print(string)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def remove_lead_zero():
    ip = "216.08.094.196"
    string = re.sub('\.[0]*', '.', ip)
    print(string)

obj = remove_lead_zero()


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
