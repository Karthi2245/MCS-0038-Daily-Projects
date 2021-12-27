# Generate all Sublist:

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
from itertools import combinations

# 1.Builtin functions
print("-----1. Built Functions--------")


# 2. Algorithm:
print("-----1. Algorithm--------")



# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def sub_lists(my_list):
    subs = []
    for i in range(0, len(my_list)+1):
      temp = [list(x) for x in combinations(my_list, i)]
      if len(temp)>0:
        subs.extend(temp)
    return subs


l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']
print("Original list:")
print(l1)
print("S")
print(sub_lists(l1))
print("Sublists of the said list:")
print(sub_lists(l1))
print("\nOriginal list:")
print(l2)
print("Sublists of the said list:")
print(sub_lists(l2))



# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class GenerateSublist:
    def sub_lists(self, my_list):
        subs = []
        for i in range(0, len(my_list) + 1):
            temp = [list(x) for x in combinations(my_list, i)]
            if len(temp) > 0:
                subs.extend(temp)
        return subs


obj = GenerateSublist()
a = obj.sub_lists([1, 3, 2, 4, 6, 7])
print(a)


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


