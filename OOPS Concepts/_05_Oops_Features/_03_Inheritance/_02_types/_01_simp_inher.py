# Single Inheritance or Simple Inheritance:

# 1 Super Class & 1 Sub Class:


class Fruit:
    def __init__(self):
        print("Each Fruit Has Different tastes")

    def sweet(self):
        print("Usually It tastes sweet when it is ripe")

class Mango(Fruit):
    def __init__(self):
        print("Mango is a Fruit")

    def color(self):
        print("The Color Of Mango is Yellow")


fruit = Fruit()
fruit.sweet()
mango = Mango()
print("Single or Simple Inheritance ".center(50,'.'))
mango.color()
mango.sweet()

# Multi Level Inheritance: 1 Super Class 1 sub class 1 sub of sub class


class Animal:
    def speak(self):
        print("Animal Speaking")


class Dog(Animal):
    def bark(self):
        print("dog barking")


class DogChild(Dog):
    def eat(self):
        print("Eating bread...")


d = DogChild()
d.bark()
d.speak()
d.eat()


class Grandfather:
    def __init__(self):
        print("Super Class".center())
        print("Grand Father has Qualties")

    def walk(self):
        print("The Grandfather has followed unique style of Walking and his "
              "son and grandson have some of his Qualities")


class Father(Grandfather):
    def __init__(self):
        print("Father has some Qualities of his father")

    def eat(self):
        print("Father has a unique eating Habits")


class Son(Father):
    def __init__(self):
        print("son has Some Quality of his father")

    def speak(self):
        print("Son's Voice is Peculiar ")


father = Father()
print("Child Class".center(40, '.'))
father.eat()
father.walk()

son = Son()
print("Child Class of Child Class".center(40, '.'))
son.speak()
son.eat()
son.walk()

# Hierarchical Inheritance:

class Mobile:
    def __init__(self):
        print("Mobile is a Super ")

    def processor(self):
        print("The Processor of the Qualcomm Snapdragon 732G ")

    def price(self):
        print("The Price of Mobile Varies")   # Generic Manner


class Motorola(Mobile):
    def __init__(self):
        print("Moto G40 Fusion is a Mobile")

    def price(self):
        print("The Price of the Phone is , 15K")


class Samsung(Mobile):
    def __init__(self):
        print("Samsung is a Mobile")

    def price(self):
        print("The Price of the Phone is , 18K")


class Realme(Mobile):
    def __init__(self):
        print("Realme is a Mobile")

    def price(self):
        print("The price of the phone is , 16K")   # Method Overriding


print("Super class".center(40, '.'))
mob = Mobile()
print("Super class".center(40, '.'))
mob1 = Motorola()
mob2 = Samsung()
mob3 = Realme()

print("Sub class1 :".center(40, '.'))
mob1.price()
mob1.processor()

# Hybrid Inheritance: Combination of Multilevel and Hierarchical:


class University:
  def __init__(self):
    print("Constructor of the Base class")
    self.univ = "MIT"

  def display(self):
    print(f"The University name is: {self.univ}")



class Course(University):
  def __init__(self):

    print("Constructor of the Child Class 1 of Class University")
    University.__init__(self)
    self.course = "CSE"

  def display(self):
    print(f"The Course name is: {self.course}")
    University.display(self)


class Branch(University):
  def __init__(self):
    print("Constructor of the Child Class 2 of Class University")
    self.branch = "Data Science"

  def display(self):
    print(f"The Branch name is: {self.branch}")


class Student(Course, Branch): # Method resolution order
  def __init__(self):
    print("Constructor of Child class of Course and Branch is called")
    self.name = "Tonny"
    Branch.__init__(self)
    Course.__init__(self)

  def display(self):
    print(f"The Name of the student is: {self.name}")
    Branch.display(self)
    Course.display(self)


ob = Student()
print()
ob.display()

# Multiple  **       : One sub class with 2 or more super classes


# Multiple Inheritance using two classes:


class Father():
    def driving(self):
        print("Father Enjoys Driving")


class Mother():
    def cooking(self):
        print("Mother Enjoys Cooking")


class Child(Father, Mother):
    def playing(self):
        print("Child Loves Playing")


c = Child()
print("Multiple Inheritance".center(40, '.'))
c.driving()
c.cooking()
c.playing()

# Creating a multiple inheritance using more than two classes.


class Car():
    def benz(self):
        print(" This is a Benz Car ")


class Bike():
    def bmw(self):
        print(" This is a BMW Bike ")


class Bus():
    def volvo(self):
        print(" This is a Volvo Bus ")


class Truck():
    def eicher(self):
        print(" This is a Eicher Truck ")


class Plane():
    def indigo(self):
        print(" This is a Indigo plane ")


class Transport(Car,Bike,Bus,Truck,Plane):
    def main(self):
        print("This is the Main Class")


b=Transport()
b.benz()
b.bmw()
b.volvo()
b.eicher()
b.indigo()
b.main()

# Performing Addition,Multiplication,Division using Multiple Inheritance


class Calculation1:
    def summation(self,a,b):
        return a+b


class Calculation2:
    def multiplication(self,a,b):
        return a*b


class Derived(Calculation1,Calculation2):
    def divide(self,a,b):
        return a/b


d = Derived()
print(d.summation(1,2))
print(d.multiplication(1,2))
print(d.divide(1,2))


# Example on Multiple Inheritance `

class Student1:
    def __init__(self):
        self.name = 'Nani'
        self.age = 19

    def get_name(self):
        return self.name


class Student2:
    def __init__(self):
        self.name = 'Ram'
        self.id = '15'

    def get_name(self):
        return self.name


class Students(Student1, Student2):
    def __init__(self):
        Student1.__init__(self)
        Student2.__init__(self)

    def getName(self):
        return self.name


Students1 = Students()

print(Students1.get_name())
