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
# 1.Builtin functions
print("-----1. Built Functions--------")

# 2. Algorithm:
print("-----1. Algorithm--------")
num = [1, 2, 3,4, 5, 6, 7, 8, 10]
odd_list = []
for i in num:
    if i % 2 == 1:
        odd_list.append(i)
print(f'The odd list is {odd_list}')

# 3 Using Functions  ==>
print("--------3 Using Functions----------")

def odd_list(num, odd):
    for i in num:
        if i % 2 == 1:
            odd.append(i)
    return odd


obj = odd_list([1,2,3,4,5,6,7,8,9,10], [])
print(f'The odd list is {obj}')

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


