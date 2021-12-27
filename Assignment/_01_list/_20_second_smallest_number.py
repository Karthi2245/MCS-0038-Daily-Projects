# Find the second smallest number in the list

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
# Second smallest number is num[1]

num = [4, 1, 5, 9, 2, 8]
num.sort()
print(num[1])
# 2. Algorithm:
print("-----1. Algorithm--------")
num = [4, 1, 5, 9, 2, 8]
for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]
print('The second largest number is', num[1])
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def secod_smallest():
    num = [4, 1, 5, 9, 2, 8]
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]
    return num[1]


obj = secod_smallest()
print('The Second smallest number is', obj)

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


