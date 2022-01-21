'''
What is FizzBuzz ?
FizzBuzz is a very simple programming problem which is asked in software
developer job interviews to determine whether the candidate knows to write code
or not.
'''
for i in range(1,101) :
    if i % 15 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else : print(i)
