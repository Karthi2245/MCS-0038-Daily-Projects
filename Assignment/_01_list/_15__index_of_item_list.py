# Find a index of an item in a specified list:
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
letter = ['a', 'b', 'c', 'd', 'e']
index = letter.index('c')
print('Index of an item', index)

# 2. Algorithm:
print("-----1. Algorithm--------")
letter = ['a', 'b', 'c', 'd', 'e']
for i in range(len(letter)):
    print('index', i, 'values', letter[i])





# 3 Using Functions  ==>
print("--------3 Using Functions----------")

def index_item():
    letter = ['a', 'b', 'c', 'd', 'e']
    for i in range(len(letter)):
        print('index', i, 'values', letter[i])


obj = index_item()


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


