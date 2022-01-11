'''
API:
API - Application Programming Interface
App - games, normal app which we have in mobile
Programming - set of instructions that u tell the computers to do certain tasks
              using that program we can build the software.
Interface - interface is a point where two app or program meet and interact with
            each other.Basically it allows to interact with one another.

Rest Frame Work - Representational state transfer
Http Methods: (to make the interaction between the machines or applications)
--> Get - to retrieve the resource
--> Post - to post the resource
--> Put - to change the resource
--> Delete- to delete the resource
It is used for the purpose of Web api for data communication

Rest API:
--> when web services use REST architecture, they are called RESTful APIs or
REST APIs.
--> A REST API is a set of web addresses that respond with pure information, not
a formatted page.
--> An API returns a JSON, which is a common format.You will see all of the
information surrounded with quotation marks, {}, [] and descriptive titles of
each bit of info.
--> json - json is a format and its not at all specify to any application

--> Rest Api installation:
--> pip install djangorestframework
--> create a project
--> create a app
--> create a model
--> register the Model in admin
--> Include rest_framework in apps which is in settings.

serializer.py:
--> serializer class is used to convert models to json data
--> In serializer.py we have to import the serializer from rest_frame
--> We have to import the .models to give it for serializer to convert into json
--> we have to create the serializer class, inside the class we have to create the
meta data for getting all the fields of models.
--> to get the model fields, we have to store the model class in a variable
after that u can store the fields value in fields value like, (fields = __all__)
--> __all__ - it return the all the value of fields.

views.py:
Class 1:(get, post)
--> first of all we have to import the all the necessary modules
--> For get and post the data we have to create the one class
--> Inside the class we have to create the get and post function.
    -> get the data from models and stored it in variable by objects.all()method
    -> After that, for serializing the value of model fields we have to send the
    model variable to serializer class and stored it in another variable.
    serializer = SerClass(model variable, many = True)
--> For post we have to get the data by request and save it with save() method
    ; serializer.save().

Class 2:(put, delete)
--> We have to get the data by id by objects.get(id=id) method.
--> After that we have to pass that id to update and delete the data.






'''
l = [1, 2, 4]
l1 = [1, 2, 4]
print(l == l1)

x=[]

x.append(10)
print(x)


print(y)

def num():
    print(x)

x = 15
z = num()

def num1():
    print(x)

num1()

