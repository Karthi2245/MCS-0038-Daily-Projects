# P01. REQ :  Format the number with percentage:


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

x = 0.25
y = -0.25
print("\nOriginal Number: ", x)
print("Formatted Number with percentage: "+"{:.0%}".format(x))
print("Original Number: ", y)
print("Formatted Number with percentage: "+"{:.0%}".format(y))
print()

# 2. Algorithm
print("-----2. Algorithm--------")
x = 0.25
if x > 0:
    y = x * 100
    print(y, "%")

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def percentage(num1):

    if num1 > 0:
        y = num1 * 100
        print(y, "%")


obj = percentage(0.35)
print("The percentage of given values", obj)




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

biscuit = 75
cream = 112