'''
Operator Overloading:
--> When an Operator can perform different actions it is said to be exhibit
polymorphism or Operator over loading.

'''
# Ex: Over loading '+' Operator :
# Using + operator to add the integers
a = 10
b = 20
c = a + b
print("The addition of two numbers", c)

# Using + operator to concatenate the string.

fname ="Karthi"
lname = "Ramesh"
name = fname + lname
print("My full name is", name)

# Ex: Adding the two objects :

class Book1:
    def __init__(self, pages):
        self.pages = pages

    # def get_pages(self): # own method
    def __add__(self, other):  # Dunder Function
        return self.pages + other.pages


class Book2:
    def __init__(self, pages):
        self. pages = pages

    # def get_pages(self):
    def __add__(self, other):
        return self.pages


tpages1 = Book1(100)
tpages2 = Book2(200)
toatlpages = tpages1 + tpages2
print("The Total Pages of two books are:", toatlpages)

# total pages = t pages1 + t pages2
# TypeError: unsupported operand type(s) for +: 'Book1' and 'Book2'


# Ex:
class Fristname:
    def __init__(self):
        self.fname = "Karthi"

    def __add__(self, other):
        return self.fname + other.lname


class Lastname:
    def __init__(self):
        self.lname = " Ramesh"

    def __add__(self, other):
        return self.lname
# Cannot two objects with their own methods

fname = Fristname()
lname = Lastname()

fullname = fname + lname
print("Fullname:", fullname)

# overloading the (>)Greater than operator:


class Tcs:
    def __init__(self):
        self.ecount = 1500

    def __gt__(self, other):
        return self.ecount > other.ecount


class Hcl:
    def __init__(self):
        self.ecount = 1300

tcs = Tcs()
hcl = Hcl()
if tcs > hcl:
    print("Tcs has More Employees")

else:
    print("Hcl has more Employees")


'''
--> ac no
--> balance
--> validate amount
--> Transfer amount # 
      --> neft 
      --> rtgs
      --> imps
'''