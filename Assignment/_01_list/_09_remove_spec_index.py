# Remove specified index from list and print

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
num = [2, 4, 6, 8, 10, 12]
new = num.pop(3)
print(num)
print("The Removed specific index", new)

# 2. Algorithm:
print("-----1. Algorithm--------")

num = [2, 4, 6, 8, 10, 12]
new = num.pop(3)
print(num)
print("The Removed specific index", new)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def remove():
    num = [2, 4, 6, 8, 10, 12]
    new = num.pop(3)
    print(num)
    print("The Removed specific index", new)


obj = remove()


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


