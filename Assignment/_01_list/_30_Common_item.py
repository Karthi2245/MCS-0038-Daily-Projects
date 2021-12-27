# Common Item in the list

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
# Using Set
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
print('The Common Item in the list :', set(color1) & set(color2))

# 2. Algorithm:
print("-----1. Algorithm--------")
color1 = ["Red", "Green", "Orange", "White"]
color2 = ["Black", "Green", "White", "Pink"]
common =[]
for i in color1:
    for j in color2:
        if i == j:
            common.append(i)

print('The Common Item in the list :', common)




# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def common(num1, num2, common):
    for i in num1:
        for j in num2:
            if i == j:
                common.append(i)

    return common


obj = common([2, 4, 6, 8], [1, 2, 4, 3, 6], [])
print('The Common Item in the list :', obj)

# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class CommonItem:
    def common(self, num1, num2, common):
        for i in num1:
            for j in num2:
                if i == j:
                    common.append(i)

        return common


common = CommonItem()
a = common.common([2, 4, 6, 8], [1, 2, 4, 3, 6], [])
print('The Common Item in the list:', a)

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


