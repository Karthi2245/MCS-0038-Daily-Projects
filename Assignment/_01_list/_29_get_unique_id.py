# Get Unique Id

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
num = 100
print('Unique Id :',format(id(num), 'x'))  # x = format Specifier
name = 'Karthikeyan'
print('Unique Id :',format(id(name), 'x'))


# 2. Algorithm:
print("-----1. Algorithm--------")
num = 100
print('Unique Id :',format(id(num), 'x'))  # x = format Specifier
name = 'Karthikeyan'
print('Unique Id :',format(id(name), 'x'))
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def unique_id():

    num = 100
    print('Unique Id :',format(id(num), 'x'))  # x = format Specifier
    name = 'Karthikeyan'
    print('Unique Id :', format(id(name), 'x'))


obj = unique_id()
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


