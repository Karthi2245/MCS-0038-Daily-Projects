# Check List has sublist or not:

'''
Topics:
--------
--> Operators
--> DM and Loops
--> Data structure
--> Crud Operations(retrieval)

# Take the string
# Remove the odd position of the string
# Write the New string in White paper
'''
# 1.Builtin functions
print("-----1. Built Functions--------")


# 2. Algorithm:
print("-----1. Algorithm--------")



# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def is_sublist(l, s):
    sub_set = False
    if s == []:
        sub_set = True
    elif s == l:
        sub_set = True
    elif len(s) > len(l):
        sub_set = False

    else:
        for i in range(len(l)):
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                if n == len(s):
                    sub_set = True

    return sub_set


a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]
print(is_sublist(a, b))
print(is_sublist(a, c))

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")
class Sublist:
    def is_sublist(self, l, s):
        sub_set = False
        if s == []:
            sub_set = True
        elif s == l:
            sub_set = True
        elif len(s) > len(l):
            sub_set = False

        else:
            for i in range(len(l)):
                if l[i] == s[0]:
                    n = 1
                    while (n < len(s)) and (l[i + n] == s[n]):
                        n += 1

                    if n == len(s):
                        sub_set = True

        return sub_set


obj = Sublist()
print(obj.is_sublist([2,4,3,5,7], [4,3]))
print(obj.is_sublist([2,4,3,5,7], [2,5]))
# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")

'''a='KIRAN kar'
b='KIRAN kar'
c='KARAN'
print(id(a),id(b),id(c))'''


