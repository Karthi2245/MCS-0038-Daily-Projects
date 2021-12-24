# P01. REQ : Longest string in python:

'''
Topics:
--------
Operators
DM vs Loops
Data structure
'''

# 0. Mathematics
# Implement the solutions in white paper

# 1.Builtin functions

print("-----1. Built Functions--------")
name = ["Karthikeyan", "Shiva", "Kumar", "Sathish"]
y = max(name, key = len)
print("The Longest String of the list :", y)


# 2. Algorithm

print("--------2. Algorithm----------")

name = ["Karthikeyan", "Shiva", "Kumar", "Sathish"]
for i in name:
    if max(name, key = len) == i:
        print("Longest string in the list :", i)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
    # I. STATE
def long():
    name = ["Karthikeyen", "Shiva", "Kumar", 'Sathish']
    for i in name:
        if max(name, key = len) == i:
            return i


long1 = long()
print("The Longest String in the list :", long1)

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class LongStr:
    def long(self):
        name = ["Karthikeyen", "Shiva", "Kumar", 'Sathish']
        for i in name:
            if max(name, key=len) == i:
                return i


long_str = LongStr()
a = long_str.long()
print(a)
# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
