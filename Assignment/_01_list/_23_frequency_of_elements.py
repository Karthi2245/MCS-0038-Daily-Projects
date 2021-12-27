# Remove even elements and print list

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
import collections
# 1.Builtin functions
print("-----1. Built Functions--------")
num = [1,2, 3, 4, 1, 3, 6, 2, 6, 5, 1]
a = collections.Counter(num)
print(a)

# 2. Algorithm:
print("-----1. Algorithm--------")
num = [1,2, 3, 4, 1, 3, 6, 2, 6, 5, 1]
new = []
count = 0
for i in range(len(num)):
    if num[i] not in new:
        new.append(i)
    for j in range(len(new)):
        if num[i] == new[j]:
            count += 1
            print(j, count)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def frequency():
    num = [1, 2, 3, 4, 1, 3, 6, 2, 6, 5, 1]
    a = collections.Counter(num)
    return a


obj = frequency()
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

'''a='KIRAN kar'
b='KIRAN kar'
c='KARAN'
print(id(a),id(b),id(c))'''


