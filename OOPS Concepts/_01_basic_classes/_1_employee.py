'''
OOPS:
--> Oops is a Object oriented  programing language that uses class and objects.
--> The concept of the  oops is to bind the data and functions together that
works on a single unit.

Object:
--> Object is something which exist physically.
--> Everything exist in the world is object and likewise everything is a object
in python.

Class:
--> Some Objects may have similar behaviour.Such object belongs to same
category called a 'Class'.
--> A class is a group name and does not exist physically.


'''

# Create a class:
class Employee:  # class
    # State
    def __init__(self, ename, eid, esys_num, enum , eaddress):
        self.ename = ename
        self.eid = eid
        self.esys_num = esys_num     # Fields
        self.enum = enum
        self.eaddress = eaddress

        # Behaviour:

    def get_emp_det(self):   # Methods
        print("Employee detail are".ljust(40, '.'), ':',self.ename, self.eid, self.esys_num,
              self.eaddress  )


emp = Employee("Karthi", "Mcs-0038", "101", "7904134297", "Bangalore" )
# object
emp.get_emp_det()



