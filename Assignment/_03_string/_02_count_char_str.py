# P01. REQ : Count the character of the string:

'''
Topics:
--------
Operators
DM vs Loops    # DM = Decision making
Data structure
'''

# 0. Mathematics
'''
# Implement the solutions in white paper
# write the characters vertically on the white paper
# Note down the count of each character. '''

# 1.Builtin functions

print("-----1. Built Functions--------")

message = 'Hello World'  # static way
for i in message:

    print("Count of the given character: ", message.count(i))
'''message = str(input("Enter the string"))
for i in message:  # Dynmaic way
    print("Count of the given character: ", message.count(i))'''

# 2. Algorithm

print("--------2. Algorithm----------")

string = 'hello world'
set1 = set(string)
dict1 = {}
for i in set1:
    dict1.update({i : 0})

for i in string:
    if i in dict1.keys():
        dict1[i] += 1
print(dict1)

# Functions:
def countchar():
    string = 'hello world'
    set1 = set(string)
    dict1 = {}
    for i in set1:
        dict1.update({i : 0})

    for i in string:
        if i in dict1.keys():
            dict1[i] += 1
    print("The Count of the Function:", dict1)


countchar()


# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
class Count_Char:
    def countchar(self):
        string = 'hello world'
        set1 = set(string)
        dict1 = {}
        for i in set1:
            dict1.update({i : 0})

        for i in string:
            if i in dict1.keys():
                dict1[i] += 1
        print("The Count of the Function:", dict1)


count = Count_Char()
count.countchar()




# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
