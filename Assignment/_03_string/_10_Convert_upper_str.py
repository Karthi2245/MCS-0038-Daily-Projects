# P01. REQ : Convert a string into Uppercase :

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
str1 = input("Enter a string:")
print("The Upper case string is".ljust(40,'.'), ':', str1.upper())
print("-----2. Algorithm--------")
# 2. Algorithm
str1 = input("Enter a lower case string:")
upper = ''
for i in range(len(str1)):
    ch = ord(str1[i])
    if ch < 96 or ch < 123:
        ch2 = chr(ch - 32)
        upper += ch2
    else:
        upper = chr(ch)
print("The Upper case string is".ljust(40, '.'), '.', upper)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def uppercase(str1, upper):
    for i in range(len(str1)):
        ch = ord(str1[i])
        if ch < 96 or ch < 123:
            ch2 = chr(ch - 32)
            upper += ch2
        else:
            upper = chr(ch)
    return upper


obj = uppercase(input("Enter a lower case string:"), '')
print("The Uppercase string is:".ljust(40, '.'), ':', obj)


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class Upper:
    def uppercase(self, str1, upper):
        for i in range(len(str1)):
            ch = ord(str1[i])
            if ch < 96 or ch < 123:
                ch2 = chr(ch - 32)
                upper += ch2
            else:
                upper = chr(ch)
        return upper


obj = Upper()
print(obj.uppercase(input('Enter a Lower case string'), ''))

# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
