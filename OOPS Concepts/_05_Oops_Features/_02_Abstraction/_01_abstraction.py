'''
Abstraction:

--> Hiding Implementation details and showing only method signature.
--> In Python, an abstraction is used to hide the irrelevant data/class in
order to reduce the complexity. It also enhances the application efficiency

'''

from abc import ABC, abstractmethod


class Car(ABC): # abstract class
    @abstractmethod
    def mileage(self): # abstract method definition
        pass



class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")

    # Driver code


t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()


class Animal:
    def __init__(self):
        print("This is Abstract Class")

    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def eat(self):
        print("Dog has Unique eating Habit") # Mandatory One

    def speak(self):
        print("Dogs are barking")


class Monkey(Animal):
    def jump(self):
        print("Monkeys are jumping Differently") # own Method

    def speak(self):
        print("Monkeys are Screaming ")


dog = Dog()
dog.eat()   # Always Create a Object for Sub Classes
dog.speak()

monkey = Monkey()
monkey.jump()
monkey.speak()



'''class Bank:
    def get_ac_info(self):'''



























