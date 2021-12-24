# P01. REQ : Move spaces to the front of a given string :

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
print("-----1. Builtin Functions--------")


# 2. Algorithm:
print("-----1. Algorithm--------")
str1 = input("Enter a string")
result = ""
str1 = result = str1.title()

for word in str1.split():
    result += word[:-1] + word[-1].upper() + " "
    print(result)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def capitalize_first_last_letters(str1):
    str1 = result = str1.title()
    result = ""
    for word in str1.split():
        result += word[:-1] + word[-1].upper() + " "
    return result[:-1]


print(capitalize_first_last_letters("python exercises practice solution"))
print(capitalize_first_last_letters("w3resource"))

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
