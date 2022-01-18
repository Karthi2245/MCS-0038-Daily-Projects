'''
# Parameterized Constructor:
--> The parameterized constructors are the constructors having a specific
number of arguments to be passed.

'''


class Student:

    def __init__(self, name, marks, subject):
        self.name = name
        self.marks = marks
        self.subject = subject

    def get_data(self):
        print("Name :", self.name,"Marks:", self.marks,"Subject:", self.subject)


data = Student("Karthi", 85, "English")
data.get_data()

# Addition:


class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        c = self.a + self.b
        print("The additon of two numbers", c)


addition = Addition(20, 30)
addition.add()


# Printing odd numbers :

class Odd:
    list_odd = [] # Class Variable

    def __init__(self, a):
        self.a = a

    def get_odd_num(self):
        for i in range(self.a):
            if i % 2 == 1:
                Odd.list_odd.append(i)
        print("The List of odd Numbers are".ljust(40, '.'), ':', Odd.list_odd)


obj = Odd(int(input("Enter Range:")))
obj.get_odd_num()

# Print Even numbers:


class Even:
    list_even = [] # Class Variable

    def __init__(self, a):  # Parameterized Constructor
        self.a = a

    def get_even_num(self):
        for i in range(self.a):
            if i % 2 == 0:
                Even.list_even.append(i)
        print("The List of Even Numbers are ".ljust(40, '.'), ':',
              Even.list_even)


obj = Even(int(input("Enter Range:")))
obj.get_even_num()

# Employee:


class Employee:
    def __init__(self, ename, eid, ephono):
        self.ename = ename
        self.eid = eid
        self.ephono = ephono

    def get_data(self):
        print("The Updated address".ljust(40, '.'), self.ename, self.eid,
              self.ephono)

    def update_address(self, eaddress):
        self.eaddress = eaddress
        print("The Updated address".ljust(40, '.'), ':', self.eaddress)


emp = Employee("Karthi", "MCS-0037", "9786910190")
emp.get_data()
emp.update_address("Banglore")
