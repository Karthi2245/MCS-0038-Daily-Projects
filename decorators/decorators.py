'''
Decorator:
-->Decorators are a highly effective and helpful Python feature because we can use
them to change the behavior of a function or class.
We use them to wrap another function in order to enhance its functionality
without having to change it permanently.
Prerequisites for Python Decorators
1. Functions are Objects in Python
-->Functions are first-class objects in Python. As a result, they have all of the
attributes of an object, and we may handle them as such by assigning them to
variables and passing them as arguments to other functions as arguments.

2. Assigning Functions to Variables in Python
In Python, we can assign a function to a variable. We can later use that
variable to call the function.
'''
# Assigning function to variable:


# Ex 2
def site():
    print("PythonGeeks")


website = site  # assigning function into variable

print(f"{site }")
print(f"{website }")
site()
website()


# Passing Function as an Argument in Python
'''
Similar to assigning functions to variables, we can also pass functions as 
arguments to other functions. The functions which accept the arguments are 
called higher-order functions.
'''


def sqrt(num):
    return num**0.5


def square(num):
    return num**2


def math(function):
    print(function(4))


math(sqrt)  # giving function as a argument
math(square)


# Function Returning Another Function in Python
'''Python also allows us to define a function that returns another function.'''


def str1():
    print("PythonGeeks")


def func1():
    return str1  # returning another function


var1 = func1()
var1()

# Nested Functions in Python
'''The Python language lets us create a function within another function.
 These enclosed functions are called nested functions'''


def math():

    def square(num):  # nested function
        return num**2

    print(square(2))


math()

# Non-local Variable and Closure in Python
'''
--> A nested function is one that is defined inside another function.
The variables of the enclosing scope can be accessed by nested functions.
These variables are called non-local variables.

--> By default, non-local variables are read-only. To modify them, we need to use a
keyword called nonlocal.

--> Closure Functions are nested functions that can access non-local variables.'''


def math(num):  # num = local variable

    def square():
        # closure function which can still access the non local variable
        return num**2

    print(square())
s

math(2)


# Decorators in Python
'''
By above all the function concepts we can create decorator
'''
# Syntax


def my_decor(func):

    def my_wrap(*args, **kwargs):
        print("Decorator Function")
        return func(*args, **kwargs)

    return my_wrap


@my_decor
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " + str2)


my_function("Mangoes", "Delicious")


# Multiple Decorators:


def my_decor(func):

    def my_wrap(*args, **kwargs):
        print("Decorator Function 1")
        return func(*args, **kwargs)

    return my_wrap


def my_another_decor(func):

    def my_wrap(*args, **kwargs):
        print("Decorator Function 2")
        return func(*args, **kwargs)

    return my_wrap

@my_decor
@my_another_decor
def my_function(str1, str2):
    print("Main Function")
    print(str1 + " are " +  str2)


my_function("Mangoes", "Delicious")


# Q1. Define a decorator that prints five ‘%’ signs before and after the
# function execution.


def dollar(func):
    def wrapper():
        print("$$$$$")
        func()
        print("$$$$$")
    return wrapper


# Q2. Define a function hello which prints “Hello World!” and decorate it with
# the dollar function without using the @ syntax.

def hello():
    print("Hello World!")


hello = dollar(hello)
hello()

# Q3. Define a function named geeks. The geeks should print
# the string “PythonGeeks”. Decorate the created function geeks with a
# decorated called dollar by using the decorator syntax.


@dollar
def geeks():
    print("PythonGeeks")

geeks()

# Q4. Define a decorator which can only work for functions with one parameter.
# The decorator should also check whether the passed argument is positive or
# not.


def deco1(func):

    def wrapper(num):
        if num >= 0:
            print("Positive")
        else:
            print("Negative")
        return func(num)
    return wrapper

# Q5. Define a decorator which can accept any number of arguments.
# The decorator should print all non-keyword arguments in a list.


def deco(func):

    def wrapper(*args, **kwargs):
        print(list(args))
        return func(*args, **kwargs)
    return wrapper