# P01. REQ :  Count Occurrences of substring


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

str1 = 'The quick brown fox jumps over the lazy dog.'
print()
print(str1.count("fox"))
print()

# 2. Algorithm
print("-----2. Algorithm--------")
message = "repeated elements are repeated again and again"
for i in message.split():  # For Comparing
    count = 0
    for j in message.split():
        if i == j:
            count = count + 1
    print(i, count)





# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def occurrence():
    message = "repeated elements are repeated again and again"
    for i in message.split():
        count = 0
        for j in message.split():
            if i == j:
                count = count + 1
        print(i, count)


obj = occurrence()

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

