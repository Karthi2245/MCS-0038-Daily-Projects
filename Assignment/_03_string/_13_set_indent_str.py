# P01. REQ :  Print following numbers with 2 dec places

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


# 2. Algorithm
import textwrap
sample_text ='''
Python is a widely used high-level, general-purpose, interpreted, dynamic
programming language. Its design philosophy emphasizes code readability,
and its syntax allows programmers to express concepts in fewer lines of
code than possible in languages such as C++ or Java.
    '''

text1 =  textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1,
                    initial_indent='',
                    subsequent_indent=' ' * 4,
                    width=80,
                    ))
print()

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def set_indent():
    sample_text ='''
    Python is a widely used high-level, general-purpose, interpreted, dynamic
    programming language. Its design philosophy emphasizes code readability,
    and its syntax allows programmers to express concepts in fewer lines of
    code than possible in languages such as C++ or Java.
        '''

    text1 =  textwrap.dedent(sample_text).strip()
    print()
    print(textwrap.fill(text1,
                        initial_indent='',
                        subsequent_indent=' ' * 4,
                        width=80,
                        ))
    print()


obj = set_indent()


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
