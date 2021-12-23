# Req: find common elements of the list:

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)

# Take the string
# Remove the odd position of the string
# Write the New string in White paper
'''
# 1.Builtin functions
print("-----1. Built Functions--------")

# 2. Algorithm:
print("-----1. Algorithm--------")
num1 = [1, 2, 3, 4, 5, 6]
num2 = [2, 4, 6, 8, 10]
for i in num1:
    for j in num2:
        if j == i:
            print("The Common Elements are", j)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def common_elements(num1, num2):
    for i in num1:
        for j in num2:
            if j == i:
                return j


obj = common_elements([2, 4, 6, 8, 10], [1, 2, 3, 4, 5, 6])


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

'''a='KIRAN kar'
b='KIRAN kar'
c='KARAN'
print(id(a),id(b),id(c))'''


