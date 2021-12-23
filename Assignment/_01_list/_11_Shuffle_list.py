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
from random import shuffle
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
shuffle(color)
print(color)
# 2. Algorithm:
print("-----1. Algorithm--------")
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
new = set(color) # set is a unordered list
print(new)




# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def shuffle_list():
    color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    new = set(color)  # set is a unordered list
    print(new)


obj = shuffle_list()
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


