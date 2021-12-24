# P01. REQ : Lower Case and Upper Case:

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)
'''

# Take the string
# Note the ASCII Value for each character of the string for Capital
    # Letters as well as small letter.
# Implement the logic on white paper
# 1.Builtin functions

print("-----1. Built Functions--------")
name = "karthi"
capital = name.upper()
print("The Capital letter of the given string".ljust(40, '.'), ':', capital)
name = "Karthi"
lower = name.lower()
print("The Lower casee of given string is".ljust(40, '.'), ':', lower)
print("-----2. Algorithm--------")
# 2. Algorithm
# convert capital letter string to small letter string
str1 = input("Enter Uppercase String:")
lower = ''
for i in range(len(str1)):
    ch = ord(str1[i])
    if ch > 64 or ch < 91:
        ch2 = chr(ch + 32)
        lower += ch2
    else:
        lower += chr(ch)

print("Lower case String is:".ljust(40, '.'), ':', lower)

# Convert small letter to capital letter:
str1 = input("Enter a lower case string:")
upper = ''
for i in range(len(str1)):
    ch = ord(str1[i])
    if ch < 96 or ch < 123:
        ch2 = chr(ch - 32)
        upper += ch2
    else:
        upper = chr(ch)

print("The Upper string is:".ljust(40, '.'), ':', upper)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")
# Convert Uppercase to Lower case


def lowercase(str1, lower):

    for i in range(len(str1)):
        ch = ord(str1[i])
        if ch > 64 or ch < 91:
            ch2 = chr(ch + 32)
            lower += ch2
        else:
            lower += chr(ch)

    return lower


obj = lowercase(input("Enter a Upper case string:"), '')
print("The Lowercase string is:".ljust(40, '.'), ':',obj)
# Covert Lowercase to Upper Case:


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


class Lower:
    def lowercase(self, str1, lower):

        for i in range(len(str1)):
            ch = ord(str1[i])
            if ch > 64 or ch < 91:
                ch2 = chr(ch + 32)
                lower += ch2
            else:
                lower += chr(ch)

        return lower


obj = Lower()
print(obj.lowercase(input('Enter a Uppercase String'), ''))



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
