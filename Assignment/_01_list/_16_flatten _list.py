# Flatten list:

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
import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
new_merged_list = list(itertools.chain(*original_list))
# * to combine all the list
print(new_merged_list)


# 2. Algorithm:
print("-----1. Algorithm--------")
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
emp = []
for i in original_list:
    a = emp.extend(i)
print(emp)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def flatten_list(num, emp):
    for i in original_list:
        a = emp.extend(i)
    return emp


obj = flatten_list([[2,4,3],[1,5,6], [9], [7,9,0]], [])
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


