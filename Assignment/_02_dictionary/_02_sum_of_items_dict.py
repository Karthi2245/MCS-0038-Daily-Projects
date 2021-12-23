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
fruit = {'mango':100, 'banana': 200, 'orange': 350, 'apple': 250}
a = sum(fruit.values())
print(a)

# 2. Algorithm:
print("-----1. Algorithm--------")
fruit = {'mango':100, 'banana': 200, 'orange': 350, 'apple': 250}
sum = 0
for i in fruit.values():
    sum = sum + i
print(sum)


# 3 Using Functions  ==>
print("--------3 Using Functions----------")
def sum_items():
    fruit = {'mango': 100, 'banana': 200, 'orange': 350, 'apple': 250}
    sum = 0
    for i in fruit.values():
        sum = sum + i
    return sum


total = sum_items()
print(total)
# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class Fruit:
    def sum_items(self):
        fruit = {'mango': 100, 'banana': 200, 'orange': 350, 'apple': 250}
        sum = 0
        for i in fruit.values():
            sum = sum + i
        return sum
obj = Fruit()
print(obj.sum_items())


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


