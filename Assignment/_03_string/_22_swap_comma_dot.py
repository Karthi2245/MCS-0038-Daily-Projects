# P01. REQ : Covert string to list:

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)
'''

# Take the string
# Remove the odd position of the string
# Write the New string in White paper
# 1.Builtin functions

print("-----1. Built Functions--------")
'''num = "32,12,228.234"
new = num.replace(",", '.')
print(new)'''
amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)
# 2. Algorithm:
print("-----1. Algorithm--------")

amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def swap_char(amount = "32.054,23"):
    maketrans = amount.maketrans
    amount = amount.translate(maketrans(',.', '.,'))
    print(amount)
    

obj = swap_char()
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
