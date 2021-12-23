# Req: Clone or Copy of List:

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
num = [2, 4,6, 8, 12,10]
c_list = num.copy()
print(f'The cloned or copy of list is {c_list}')
# 2. Algorithm:
print("-----1. Algorithm--------")
num = [2, 4,6, 8, 12,10]
c_list = []
for i in num:
    c_list.append(i)
print(f'The cloned or copy of list is {c_list}')


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def clone(num):
    c_list = []
    for i in num:
        c_list.append(i)
    return c_list


obj = clone([1, 3, 5, 7, 9])
print(f'Cloned odd lists are {obj}')

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


