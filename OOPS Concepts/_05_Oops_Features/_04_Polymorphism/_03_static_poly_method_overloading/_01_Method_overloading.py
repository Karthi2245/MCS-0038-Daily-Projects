'''
Method overloading:
--> If a method is written in way that can perform more than one task , it is
called Method Overloading.
--> python Doesn't Support method support Method over loading.But we can
achieve method overloading by writing the same method with several parameters.
'''
# Ex:
class Addition:
    def __init__(self, a = None , b = None, c = None):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        print(self.a + self.b + self.c)
# Positional Arguments:


addition = Addition(100, 200, 300)   # Method Over Loading for Integers
addition.add()

addition = Addition(12.5, 20.5, 30.5)  # Method over Loading for Float
addition.add()

addition = Addition("Karthi", "Keyan", "Ramesh")  # For String
addition.add()

# Default Arguments:

class Addition:
    def __init__(self, a, b = 10, c = 20):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        print(self.a + self.b + self.c)
# :


addition = Addition(30)   # Default Arguments
addition.add()

addition = Addition(30, 10)
addition.add()

addition = Addition(c = 12, b = 15, a = 25) # Key Word Arguments
addition.add()

