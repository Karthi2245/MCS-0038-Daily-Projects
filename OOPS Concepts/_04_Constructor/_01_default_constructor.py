'''
Constructor:
--> Constructor is a special method that is used to intialize the instance
variables of a class.

--> First Parameter will be 'self' variable that contains the memory address of
the instance.

Default Constructor:
--> The Default Constructor defined as that the constructor which has no
parameter,but has special parameter called 'Self'.

'''
# Ex:


class Student:

    def __init__(self):
        self.name = "Karthi"
        self.marks = 98
        self.subject = "Maths"

    def get_data(self):
        print("Name :", self.name,"Marks:", self.marks,"Subject:", self.subject)


data = Student()
data.get_data()

# Addition:


class Addition:
    def __init__(self):
        self.a = 10
        self.b = 20

    def add(self):
        c = self.a + self.b
        print("The additon of two numbers", c)


addition = Addition()
addition.add()


# Printing odd numbers :

class Odd:
    list_odd = [] # Class Variable

    def __init__(self):
        self.a = int(input("Enter The Range: "))

    def get_odd_num(self):
        for i in range(self.a):
            if i % 2 == 1:
                Odd.list_odd.append(i)
        print("The List of odd Numbers are".ljust(40, '.'), ':', Odd.list_odd)


obj = Odd()
obj.get_odd_num()

# Print Even numbers:


class Even:
    list_even = [] # Class Variable

    def __init__(self):  # Default Constructor
        self.a = int(input("Enter the range :"))

    def get_even_num(self):
        for i in range(self.a):
            if i % 2 == 0:
                Even.list_even.append(i)
        print("The List of Even Numbers are ".ljust(40, '.'), ':',
              Even.list_even)


obj = Even()
obj.get_even_num()

# Employee:


class Employee:
    def __init__(self):
        self.ename = "Karthi"
        self.eid = "MCS-0037"
        self.ephono = "9786910190"

    def get_data(self):
        print("The Updated address".ljust(40, '.'), self.ename, self.eid,
              self.ephono)

    def update_address(self):
        self.eaddress = "Banglore"
        print("The Updated address".ljust(40, '.'), ':', self.eaddress)


emp = Employee()
emp.get_data()
emp.update_address()
