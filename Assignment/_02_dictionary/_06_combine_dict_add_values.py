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
from collections import Counter
num1 = {'a': 25, 'b': 30, 'c': 50}
num2 = {'a': 40, 'b': 15, 'c': 75}
value = Counter(num1)+ Counter(num2)
print(value)

# 2. Algorithm:
print("-----1. Algorithm--------")

num1 = {'a': 25, 'b': 30, 'c': 50}
num2 = {'a': 40, 'b': 15, 'c': 75}

for key in num1:
    if key in num2:
        num1[key] = num1[key] + num2[key]
print(num1)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")

def combine():
    num1 = {'a': 25, 'b': 30, 'c': 50}
    num2 = {'a': 40, 'b': 15, 'c': 75}

    for key in num1:
        if key in num2:
            num1[key] = num1[key] + num2[key]
    print(num1)


obj = combine()

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class Combine:
    def combine(self):
        num1 = {'a': 25, 'b': 30, 'c': 50}
        num2 = {'a': 40, 'b': 15, 'c': 75}

        for key in num1:
            if key in num2:
                num1[key] = num1[key] + num2[key]
        print(num1)

obj1 = Combine()
obj1.combine()


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


