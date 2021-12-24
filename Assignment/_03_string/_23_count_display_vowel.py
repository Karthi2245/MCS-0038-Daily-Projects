# P01. REQ : Count and Display the vowels in given string:

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


# 2. Algorithm:
print("-----1. Algorithm--------")
vowels = "a, e, i, o, u"
name = "Karthikeyan"
for i in vowels:
    count = 0
    for j in name:
        if i == j:
            print(i)
            count += 1
            print((i, count))

"""vowels = "aeiuoAEIOU"
text = input("Enter a Text")
print(len([letter for letter in text if letter in vowels]))
print([letter for letter in text if letter in vowels])"""




# 3 Using Functions  ==>
print("--------3 Using Functions----------")
'''def display_vowel(vowels, name):
    for i in vowels:
        count = 0
        for j in name:
            if i == j:
                 
            
                print(i)
                count += 1
        print((i, count))
obj = display_vowel("a,e,i,o,u", "Hello everyone i welcome you to my world")'''


def vowel(text):
    vowels = "aeiuoAEIOU"
    print(len([letter for letter in text if letter in vowels]))
    print([letter for letter in text if letter in vowels])


vowel('Karthikeyan')


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
