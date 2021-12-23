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


# 2. Algorithm:
print("-----1. Algorithm--------")

my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
for row in zip(*([key] + (value) for key, value in sorted(my_dict.items()))):
    print(*row)



# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def table():
    my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
    for row in zip(
            *([key] + (value) for key, value in sorted(my_dict.items()))):
        print(*row)

obj = table()


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
class Table:
    def table(self):
        my_dict = {'C1': [1, 2, 3], 'C2': [5, 6, 7], 'C3': [9, 10, 11]}
        for row in zip(
                *([key] + (value) for key, value in sorted(my_dict.items()))):
            print(*row)

obj = Table()
obj.table()

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


