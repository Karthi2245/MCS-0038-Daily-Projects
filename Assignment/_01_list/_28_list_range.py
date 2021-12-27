# Create a list by concatenating a given list which range goes from 1 to n

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
my_list = ['p', 'q']
n = 4
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def list_range():
    my_list = ['p', 'q']
    n = 4
    new_list = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in my_list]
    print(new_list)


obj = list_range()

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class ListRange:
    def list_range(self):
        my_list = ['p', 'q']
        n = 4
        new_list = ['{}{}'.format(x, y) for y in range(1, n + 1) for x in
                    my_list]
        print(new_list)


a = ListRange()
a.list_range()

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


