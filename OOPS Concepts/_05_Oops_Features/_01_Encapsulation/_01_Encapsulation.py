'''
Encapsulation:
--> Binding the data members and member methods into single entity.
--> In simple words writing attributes and methods inside a class.
'''
# EX:  Normal creation of a class is example of Encapsulation


class Student:

    def __init__(self):
        self.id = 10
        self.name = 'Raju'

    def display(self):
        print("The Detail of student:", self.id, self.name)


data = Student()
data.display()

class Employee:

    def __init__(self):

        self.name = 'Karthi'
        self.id = "MCS-0037"
        self.phono = "9786910190"
        self.address = "Banglore"

    def get_data(self):
        print("The Detail of student:", self.id, self.name, self.phono,
              self.address)


data = Employee()
data.get_data()
