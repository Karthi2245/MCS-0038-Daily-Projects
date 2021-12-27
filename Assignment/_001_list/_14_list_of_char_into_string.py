# Covert List of character into string:

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
name = ['K', 'a', 'r', 't', 'h', 'i']
str1 = ''.join(name)
print(str1)

# 2. Algorithm:
print("-----1. Algorithm--------")
name = ['K', 'a', 'r', 't', 'h', 'i']
str1 = ''
for i in name:
    str1 = str1 + i
print(str1)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def char_string(name):
    str1 = ''
    for i in name:
         str1 = str1 + i
    return str1


obj = char_string(['K', 'a', 'r', 't', 'h', 'i'])

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


