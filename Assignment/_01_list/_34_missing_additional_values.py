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
list1 = ['a','b','c','d','e','f']
list2 = ['d','e','f','g','h']
print('Missing values in second list: ', ','.join(set(list1).difference(list2)))
print('Additional values in second list: ', ','.join(set(list2).difference(list1)))
# 2. Algorithm:
print("-----1. Algorithm--------")




# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def missing_additional():


    list1 = ['a', 'b', 'c', 'd', 'e', 'f']
    list2 = ['d', 'e', 'f', 'g', 'h']
    print('Missing values in second list: ',
          ','.join(set(list1).difference(list2)))
    print('Additional values in second list: ',
          ','.join(set(list2).difference(list1)))



obj = missing_additional()

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


