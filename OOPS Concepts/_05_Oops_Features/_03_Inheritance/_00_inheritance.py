'''
Inheritance:

--> Inheritance allows us to define a class that inherits all the methods and
properties from another class.

--> Parent class is the class being inherited from, also called base class.

--> Child class is the class that inherits from another class, also called
derived class.

USes:
--> We can inherit the methods of Super class to sub class,so code reusability
is possible

--> It avoids Code Duplication too.
when to use:
inheritance = is a relationship
aggregation = has a relationship

'''

# Ex: is a relation ship:

class Electronics:
    def __init__(self):
        print("This is a super class")

    def heating_up(self):
        print("The electronics item will be heating up very soon")


class Refrigerator(Electronics):
    def __init__(self):
        print("Refrigerator is a Electronic item")

    def volatge(self):
        print("It uses 120v")


class Mobile(Electronics):
    def __init__(self):
        print("Mobile is a Electronic Item")

    def capacity(self):
        print("It has a battery capacity of 6000mah")


class Tv(Electronics):
    def __init__(self):
        print("Tv is a Electronic item")

    def cable(self):
        print("The amount of cable for a month is 250Rs.")

print("Sub Class 1".center(40, '.'))
ref = Refrigerator()
ref.volatge()
ref.heating_up()

print("Sub Class 2".center(40, '.'))
mob = Mobile()
mob.heating_up()

print("Sub class 3".center(40, '.'))
tv = Tv()
tv.cable()
tv.heating_up()

# This is Example of method overriding


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

print("Sub class2 :".center(40, '.'))
mob2.price()
mob2.processor()

print("Sub class3 :".center(40, '.'))
mob3.price()
mob3.processor()
