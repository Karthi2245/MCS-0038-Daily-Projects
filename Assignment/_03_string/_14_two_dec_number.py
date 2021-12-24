# P01. REQ :  Print following numbers with 2 dec places

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
num = 2.154327
format_float = "{:.2f}".format(num)
print(format_float)
# 2. Algorithm
print("-----2. Algorithm--------")
float = 2.154327
format_float = "{:.2f}".format(float)
print(format_float)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def format_float(num = 2.154327):
    num = "{:.2f}".format(num)
    return num


obj = format_float()

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
