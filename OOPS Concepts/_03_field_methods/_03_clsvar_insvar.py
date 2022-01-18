'''
Class Variable:
--> The Variable which is created inside the class.

--> We can access the class variable anywhere in the class and any method
inside the class can access the class variable.

--> The better way to access the Class variable is "class name.variable name"

--> But we can also access the variable using self keyword too.
"self.variable name"

'''


class Addition:

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):

        add1 = self.a + self.b + self.c
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 40 # Class Variable

    def __init__(self, a, b, c):
        self.a = a  # Instance Variable
        self.b = b  # Instance Variable
        self.c = c  # Instance Variables

    def add(self):  # Instance Method
        add1 = self.a + self.b + self.c + Addition.d
        # Class Variable accessing Method 1
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 50

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        add1 = self.a + self.b + self.c + self.d
        '''self.d --> since its a Class Variable so we can access this using 
        self object'''
        return add1


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add())


class Addition:
    d = 70
    e = 80

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        add1 = self.a + self.b + self.c
        return add1

    @classmethod
    def getadd(cls):  # --> This is the syntax to get the class method
        add2 = Addition.d + Addition.e
        return add2


x = Addition(20, 30, 40)
print("The addition".ljust(40, '.'), ':', x.add() + x.getadd())
print("Hello Everyone".ljust(40, '.'),': ' , x.add())



