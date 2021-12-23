# Remove even elements and print list

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
num1 = [20, 30, 40, 50]
num2 = [15, 25, 35, 45]
res1 = 0
res2 = 0
for i in range(len(num1)):
    res1 += num1[i]
for j in range(len(num2)):
    res2 += num2[j]

difference = res1 - res2
print("The difference of the two list:", difference)



# 3 Using Functions  ==>
print("--------3 Using Functions----------")


def difference(num1, num2):
    res1 = 0
    res2 = 0
    for i in range(len(num1)):
        res1 += num1[i]
    for j in range(len(num2)):
        res2 += num2[j]

    differ = res1 - res2
    return differ


obj = difference([20, 30, 40, 50], [15, 25, 35, 45])
print(f'The differnce of two list is: {obj}')


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

'''a='KIRAN kar'
b='KIRAN kar'
c='KARAN'
print(id(a),id(b),id(c))'''


