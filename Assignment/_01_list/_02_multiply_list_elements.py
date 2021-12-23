# Req: Multiplication of element of list:
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
result = 1
num = [10,30, 25, 35]
for i in range(len(num)):
    result *= num[i]
print("The multiplication of list elements", result)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def mul_list():
    num = [10, 30, 25, 35]
    result = 0
    for i in range(len(num)):
        result *= num[i]
    print("The multiplication of the list elements", result)


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


a='KIRAN kar'
b='KIRAN kar'
c='KARAN'
print(id(a),id(b),id(c))


