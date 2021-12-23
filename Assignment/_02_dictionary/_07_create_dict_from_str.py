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

from collections import defaultdict, Counter
str1 = 'Karthi'
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)

# 2. Algorithm:
print("-----1. Algorithm--------")

string = "{'A':13, 'B':14, 'C':15}"

# eval() convert string to dictionary
Dict1 = eval(string)
print(Dict1)



# 3 Using Functions  ==>
print("--------3 Using Functions----------")

def convert_dict():
    string = "{'A':13, 'B':14, 'C':15}"
    Dict1 = eval(string)
    print(Dict1)


obj = convert_dict()


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
class Convert:
    def convert_dict(self):
        string = "{'A':13, 'B':14, 'C':15}"

        # eval() convert string to dictionary
        Dict1 = eval(string)
        print(Dict1)

obj1 = Convert()
obj1.convert_dict()


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


