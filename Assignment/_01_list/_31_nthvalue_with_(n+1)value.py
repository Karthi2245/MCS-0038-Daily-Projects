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
from itertools import zip_longest, chain, tee

# 1.Builtin functions
print("-----1. Built Functions--------")


# 2. Algorithm:
print("-----1. Algorithm--------")



# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def replace2copy(lst):
    lst1, lst2 = tee(iter(lst), 2)
    return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))


n = [0, 1, 2, 3, 4, 5]
print(replace2copy(n))


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class ChangePosition:
    def replace2copy(self, lst):
        lst1, lst2 = tee(iter(lst), 2)
        return list(chain.from_iterable(zip_longest(lst[1::2], lst[::2])))


obj = ChangePosition()
print(obj.replace2copy([0, 1, 2, 3, 4, 5]))


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


