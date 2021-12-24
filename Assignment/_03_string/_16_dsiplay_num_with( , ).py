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

x = 3000000
y = 30000000
print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x))
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y))
print()

# 2. Algorithm
print("-----2. Algorithm--------")

x = 3000000
y = 30000000
print("\nOriginal Number: ", x)
print("Formatted Number with comma separator: "+"{:,}".format(x))
print("Original Number: ", y)
print("Formatted Number with comma separator: "+"{:,}".format(y))
print()

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def comma(num1, num2):

    print("\nOriginal Number: ", x)
    print("Formatted Number with comma separator: "+"{:,}".format(num1))
    print("Original Number: ", y)
    print("Formatted Number with comma separator: "+"{:,}".format(num2))


obj = comma(20000000, 2000)




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