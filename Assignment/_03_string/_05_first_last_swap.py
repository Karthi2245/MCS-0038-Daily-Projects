# P01. REQ : First and last letter swap:

'''
Topics:
--------
Operators
Data structure
Crud Operations(retrieval)
'''

# Take the string
# First change the first value of the string as last value
# Then change the second value of the string as first value
# Write the new string in white paper

# 1.Builtin functions

print("-----1. Built Functions--------")
# 2. Algorithm

print("--------2. Algorithm----------")
name = "Karthikeyan"
first = name[0]
last = name[-1]
reverse = last + name[1:-1] + first # to access the string  use slice operation
print("The New string is", reverse)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def swap():
    name = "Karthikeyan"
    first = name[0]
    last = name[-1]
    reverse = last + name[1:-1] + first
    # to access the string  use slice operation
    return reverse


obj = swap()
print("The New String is :", obj)

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class Swap:
    def swap(self):
        name = "Karthikeyan"
        first = name[0]
        last = name[-1]
        reverse = last + name[1:-1] + first
        # to access the string  use slice operation
        return reverse


obj = Swap()
print('The New String is:', obj.swap())


# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
