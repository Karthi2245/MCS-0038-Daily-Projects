# Req: Remove Duplicate element of the list:

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
num = [10, 20, 10, 25, 45, 20]
a = set(num)
print(f'The New Removed list is:{a}')

# 2. Algorithm:
print("-----1. Algorithm--------")
num = [10, 20, 10, 25, 45, 20]
emp =[]
for i in num:
    if i not in emp:
        emp.append(i)
print(f'The New Removed list is:{emp}')

# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def remove_duplicate(str1):

    emp = []
    for i in num:
        if i not in emp:
            emp.append(i)
    return emp


obj = remove_duplicate(["Karthi", "shiva", "kumar", "Karthi", "kumar"])
print("The Removed string list:", obj)



# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")

class Remove_Duplicate:
     def duplicate(self):
         num = [10, 20, 10, 25, 45, 20]
         emp = []
         for i in num:
             if i not in emp:
                 emp.append(i)
         return emp


obj = Remove_Duplicate()
a = obj.duplicate()
print(a)




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


