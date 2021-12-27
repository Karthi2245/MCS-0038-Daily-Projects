# Append a list to another list

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
num = [1, 2, 3, 0]
color = ['Red', 'Green', 'Black']

num.extend(color)
print(num)

# 2. Algorithm:
print("-----1. Algorithm--------")

list1 = [1, 2, 3, 0]
list2 = ['Red', 'Green', 'Black']
final_list = list1 + list2
print(final_list)



# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def append_list(num, color):
    final_list = num + color
    return final_list


obj = append_list([1, 2, 3, 0], ['Red', 'Green', 'Black'])
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


