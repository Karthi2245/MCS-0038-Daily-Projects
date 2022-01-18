'''
Self:
--> Self is key word which represents the instance of the class.
--> By using the “self” keyword we can access the attributes and methods of the
 class in python
--> Self is a object which wraps the instance variables.
--> Self is a Special parameter.
--> We should declare instance methods or function using self parameter only
'''
# Ex:


class Person:

      def __init__(self, name, age):

        self.name = name
        self.age = age

      def myfunc(self):
          print("Hello my name is " + self.name)


p1 = Person("John", 36)


p1.myfunc()















