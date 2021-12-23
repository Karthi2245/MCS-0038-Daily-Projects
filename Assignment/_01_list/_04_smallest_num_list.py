# Req: Largest number of list:
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
num = [10,30, 45, 35]
largest = min(num)
print("The smallest number of the list", num)
# 2. Algorithm:
print("-----1. Algorithm--------")
'''num = [10,30, 45, 35]
for i in range(len(num)):
    for j in range (len(num)):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]
print("The smallest number of the list", num[-1])'''

num = [10,30, 45, 35]
a = num[0]
for i in range(len( num)):
    if num[i] < a:
        a = num[i]
print(f'The smallest number of the list: {a}')

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def largest(num):
    a = num[0]
    for i in range(len(num)):
        if num[i] < a:
            a = num[i]
    return a


obj = largest([25, 23, 90, 88])
print("The smallest number of the list:", obj)



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


