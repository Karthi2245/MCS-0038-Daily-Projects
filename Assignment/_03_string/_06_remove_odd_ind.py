# P01. REQ : Remove odd index:

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


print("-----2. Algorithm--------")
# 2. Algorithm
'''name = "Karthi"
for i in name:
    if name.index(i) % 2 == 0:
        print(str(i))'''
str1 = "Karthi"
result = ""
for i in range(len(str1)):

    if i % 2 == 0:
        result = result + str1[i]
print(result)

# 3 Using Functions  ==>
print("--------3 Using Functions----------")
'''def remove_odd():
    name = "Karthi"
    for i in name:
        if name.index(i) % 2 == 0:
            print("The New string is ", str(i))
obj = remove_odd()'''


def odd_values_string(str):
  result = ""
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result


print(odd_values_string('Karthi'))
print(odd_values_string('Shiva'))



# 4 OOPS  ==> 5
print("--------4 Object Oriented----------")


class RemoveOddIndex:
    def odd_values_string(self, str):
        result = ""
        for i in range(len(str)):
            if i % 2 == 0:
                result = result + str[i]
        return result


obj = RemoveOddIndex()
print('The New string is : ', obj.odd_values_string('Karthikeyan'))

# 5 Exception handling  ==> 2
print("--------5 Exception handling----------")
# 6 File Handling  ==> 1
print("--------6 File Handling----------")
# 6 Database interaction MVC  ==> 1
print("--------6 Database interaction----------")
# 7 UI Interaction   ==> 1
print("--------7 UI Interaction----------")
