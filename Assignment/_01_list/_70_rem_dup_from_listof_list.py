# Remove the duplicate elements of the list of lists

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

num = [[1, 2], [3, 4], [1,2], [2,3], [5, 6], [2,3]]
for i in num:
    print(i)

# 2. Algorithm:
print("-----1. Algorithm--------")

num = [[1, 2], [3, 4], [1,2], [2,3], [5, 6], [2,3]]
new = []

for i in num:
    if i not in new:
        new.append(i)
print(new)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def Merge(dict1, dict2):
    res = dict1.update(dict2)
    return res


dict1 = {'x': 10, 'y': 8}
dict2 = {'a': 6, 'b': 4}
dict3 = Merge(dict1, dict2)
print(dict1)



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
