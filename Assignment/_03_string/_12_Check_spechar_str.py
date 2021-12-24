# P01. REQ :  check whether a string starts with specified characters

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
message = "@ Welcome to Python"
msge = message.startswith("@")
print(msge)

# 2. Algorithm
print("-----2. Algorithm--------")
message = "@ Welcome to Python"
msge = message.startswith("@")
print(msge)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")

def spechar():
    message = "@ Welcome to Python"
    msge = message.startswith("@")
    return msge


obj = spechar()
print(obj)


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
