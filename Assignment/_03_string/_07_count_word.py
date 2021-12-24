# P01. REQ : Count Word:

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


print("-----2. Algorithm--------")
# 2. Algorithm
name = "I am a super class"
str1 = name.split()
str2 = len(str1)
print("The Count of Words", str2)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
# Python3 program to count words


def count_word():

    name = "I am a super class"
    str1 = name.split()
    str2 = len(str1)
    return str2


x = count_word()
print("The Count of Words", str2)

# This code is contributed by BHAVYA JAIN


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class CountWord:

    def count_word(self):
        name = "I am a super class"
        str1 = name.split()
        str2 = len(str1)
        return str2


obj = CountWord()
print('The Count of Word',obj.count_word() )
# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
