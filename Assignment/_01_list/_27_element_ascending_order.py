# Printing Element in the Ascending Order

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
num = [2, 1, 3, 5, 7, 8, 4]
num.sort()
print('The ascending num of list is',num)
# 2. Algorithm:
print("-----1. Algorithm--------")
num = [2, 1, 3, 5, 7, 8, 4]
for i in range(len(num)):
    for j in range(len(num)):
        if num[i] < num[j]:
            num[i], num[j] = num[j], num[i]
print('The ascending order of the List is:', num)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def ascending_order():
    for i in range(len(num)):
        for j in range(len(num)):
            if num[i] < num[j]:
                num[i], num[j] = num[j], num[i]
    return num


obj = ascending_order()
print('The ascendig order of the List:', obj)
# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class Ascending:
    def ascending_order(self):
        for i in range(len(num)):
            for j in range(len(num)):
                if num[i] < num[j]:
                    num[i], num[j] = num[j], num[i]
        return num


obj = Ascending()
a = obj.ascending_order()
print('The Ascending order of the List', a)

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


