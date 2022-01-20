'''Task
The provided code stub reads two integers from STDIN, a and b. Add code to
print three lines where:

--> The first line contains the sum of the two numbers.
--> The second line contains the difference of the two numbers (first - second).
--> The third line contains the product of the two numbers.
Example
a = 3
b = 5
Print the following:

8 -> add
-2 -> sub
15 -> multi
'''

a = int(input('Enter an Integer :'))
b = int(input('Enter an Integer :'))

if a > 0 and b > 0:
    c = a+b
    print(c)
    c = a-b
    print(c)
    c = a*b
    print(c)


