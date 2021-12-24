# P01. REQ : Convert a string in to Uppercase :

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)


--> Use the strip() Function to Remove a Newline Character From the String in Python.
--> Use the replace() Function to Remove a Newline Character From the String in Python.
--> Use the re.sub() Function to Remove a Newline Character From the String in Python
'''

# Take the string
# Remove the odd position of the string
# Write the New string in White paper
# 1.Builtin functions

print("-----1. Built Functions--------")


# 2. Algorithm
print("-----2. Algorithm--------")
sample_list = ["a", "b\n", "c\n"]
converted_list = []

for element in sample_list:
    converted_list.append(element.strip())

print(converted_list)
# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def remove_newline(sample_list, converted_list):

    for element in sample_list:
        converted_list.append(element.strip())
    return converted_list


obj = remove_newline(["a", "b\n", "c\n"], [])
print(converted_list)




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
