# Create a Multiple list:

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


# 2. Algorithm:
print("-----1. Algorithm--------")

obj = {}
for i in range(1, 21):
    obj[str(i)] = []
print(obj)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def create():
    obj = {}
    for i in range(1, 21):
        obj[str(i)] = []
    return obj


obj =create()
print(obj)

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class Create:
    def create(self):
        obj = {}
        for i in range(1, 21):
            obj[str(i)] = []
        return obj


obj = Create()
print(obj.create())
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


