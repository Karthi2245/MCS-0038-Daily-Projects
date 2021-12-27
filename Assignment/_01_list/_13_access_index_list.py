# Access the index of the list:

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
# Enumerate Function:
letter = ['a', 'b', 'c', 'd', 'e']
for index, values in enumerate(letter):
    print('Index',index,'Values', values)
# Zip Function:
print('Using Zip Function')
for index , values in zip(range(len(letter)),letter):
    print('Index',index,'values', values)

# 2. Algorithm:
print("-----1. Algorithm--------")

employee =['Karthi', 'Shiva', 'Kumar', 'Karthick']
for i in range(len(employee)):
    print('Index', i,'Values', employee[i])


# 3 Using Functions  ==>
print("--------3 Using Functions----------")

def access_index():
    employee = ['Karthi', 'Shiva', 'Kumar', 'Karthick']
    for i in range(len(employee)):
        print('Index', i, 'Values', employee[i])


obj = access_index()


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


