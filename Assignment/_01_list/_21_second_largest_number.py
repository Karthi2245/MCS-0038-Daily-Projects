# Second Largest number in the list

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
# second largest number is num[-2]
num = [2, 1, 4, 9, 3, 8]
num.sort()
print('The Second Largest number is', num[-2])
# 2. Algorithm:
print("-----1. Algorithm--------")
num = [2, 1, 4, 9, 3, 8]
for i in range(len(num)):
    for j in range (len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]
print("The second Largest number of the list", num[-2])

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def second_largest():
    num = [2, 1, 4, 9, 3, 8]
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]
    return num[-2]


obj = second_largest()
print('The Seond Smallest number is', obj)

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


