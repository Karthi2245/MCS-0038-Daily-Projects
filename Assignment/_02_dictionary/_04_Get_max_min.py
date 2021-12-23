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
num = {'a': 115, 'b': 95, 'c': 155, 'd': 250}
maximum = max(num.values())
minmum = min(num.values())
print(maximum)
print(minmum)
# 2. Algorithm:
print("-----1. Algorithm--------")


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
# code
# Python code to merge dict using a single
# expression
def max_min():
    num = {'a': 115, 'b': 95, 'c': 155, 'd': 250}
    maximum = max(num.values())
    minmum = min(num.values())
    return minmum, maximum

obj = max_min()
print(obj)

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class Max_Min:
    def max_min(self):
        num = {'a': 115, 'b': 95, 'c': 155, 'd': 250}
        maximum = max(num.values())
        minmum = min(num.values())
        return minmum, maximum

obj = Max_Min()
max_min = obj.max_min()
print(max_min)


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


