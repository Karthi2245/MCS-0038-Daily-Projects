# Get Unique Values in list

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
# get unique values of the list is nothing but removing repeated elements:
num = [1, 4, 2, 4, 1, 5, 6, 5]
new_num = set(num)
list1 = list(new_num)
print('Unique values of list is: ', list1)
# 2. Algorithm:
print("-----1. Algorithm--------")
num = [1, 4, 2, 4, 1, 5, 6, 5]
new = []
for i in num:
    if i not in new:
        new.append(i)
print('The Unique values of list is: ', new)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def unique(num, new):
    for i in num:
        if i not in new:
            new.append(i)
    return new


obj = unique([1, 4, 2, 4, 1, 5, 6, 5], [])
print('The Unique values of list is: ', obj)





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


