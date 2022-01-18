'''
Polymorphism:
Polymorphism Means doing same tasks in many forms.


# Constructor Overloading:
--> If We can Create the object for the class in many ways by giving some value
to the parameters are called Constructor Over Loading.
'''

class Mobile:
    def __init__(self, price, manufacture, brand ="samsung",model="Galaxy M32"):
        self.price = price
        self.manufacture = manufacture
        self.brand = brand
        self.model = model

    def get_data(self):
        print(self.price, self.manufacture, self.brand, self.model)


mob = Mobile(10000, 2018)
mob = Mobile(10000, 2018, "samsung")
mob = Mobile(10000, 2018, "samsung", "Galaxy M32")

mob.get_data()

class Employee:
    def __init__(self, eid, ename = "Karthi", eaddress = "Banglore"):
        # we cannot create non self parameter after default parameter.
        self.eid = eid
        self.ename = ename
        self.eaddress = eaddress

    def display(self, ephone = 9786910190):  # Method Overloading
        print(self.eid, self.ename, self.eaddress, ephone)


emp = Employee("Mcs-0038")
emp.display()
emp = Employee("MCS-0038", "Karthi")
emp = Employee("MCS-0038", "Karthi","Banglore")
emp.display()

class Addition:
    def __init__(self, a = 10, b = 20, c = 30):
        self.a = a
        self.b = b
        self.c = c

    def add(self):
        print("The Addition of the three Numbers", self.a + self.b + self.c )


obj = Addition()
obj.add()

obj = Addition(10)
obj.add()

obj = Addition(10, 20)
obj.add()

obj = Addition(10, 20, 30)









































