# P01. REQ : Covert string to list:

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)
'''

# Take the string
# Remove the odd position of the string
# Write the New string in White paper
# 1.Builtin functions

print("-----1. Built Functions--------")
name = "Karthi"
list1 = list(name.split())
print(list1)

# 2. Algorithm:
print("-----1. Algorithm--------")
name = "Karthi"
list1 = []
list1.append(name)
print(list1)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def convert_list():
    name = "Karthi"
    list1 = []
    list1.append(name)
    print(list1)


obj = convert_list()


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
