'''
Decorators:
--> Python has an interesting feature called decorators to add functionality
to an existing code.
--> This is also called meta programming because a part of the program tries to
modify another part of the program at compile time.
'''
# Without Decorators:
# Ex: 1

def first(msg):
    print(msg)


first('hello')
second = first
second('hello')

# Ex:2


def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


x = operate(inc, 3)
print(x)
x = operate(dec, 4)
print(x)


def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()

# Outputs "Hello"
new()

# with decorators:


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


@make_pretty  # Decorator
def ordinary():
    print("I am ordinary")
# ordinary()
# pretty = make_pretty(ordinary)  # This is one way
# pretty()


ordinary()

# Decorating Functions with parameters:


def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return

        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    print(a/b)


divide(10, 2)

# Chain Decorators:


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Hello")


# Assignment:
num = int(input("Enter the Number"))
n = int(input("Enter the range"))
list1 = [i for i in range(1, n)]
for i in list1:
    for j in list1:
        if i <= num/2:
            if i + j == num:
                a = i, j
                tuple(a)
                print(a)






































