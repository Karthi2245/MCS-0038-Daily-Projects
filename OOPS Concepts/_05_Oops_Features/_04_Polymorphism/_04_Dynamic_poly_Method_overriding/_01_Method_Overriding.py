'''
Method Overloading:
--> When There is a method in super class , writing the same the same method in
sub class so that it is replaces the super class method is called
Method Overriding.

'''


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

class Bank:
    def __init__(self):
        print(" I am a Super Class")

    def branch(self):  # The Method which need to override.
        print("Sub class Can override me")

class Icici:
    def branch(self):
        print("I am in Banglore")

    def customers(self):
        print("I have 1million Customers")

class Sbi(Bank):
    def branch(self):
        print("I am in Chennai")

    def atm(self):
        print("I have Atm at all the Locations")

bank = Sbi()
bank.branch()

bank = Icici()
bank.customers()
bank.branch()


