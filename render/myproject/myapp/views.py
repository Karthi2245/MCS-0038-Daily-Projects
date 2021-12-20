from django.shortcuts import *
from django.views import View


# Create your views here.


def my_fun(request):
    return HttpResponse('This is my basic Function')


def my_template(request):  # using html template in views.py
    # create a variable:
    response = ''' <p> This is my html template</p>'''
    return HttpResponse(response)

# after creating a function...just set the path in app/urls.py

# with dynamic variable:


def my_temp(request, page):
    response = '''<h2> This is my HTML Template which has</h2>'''+ page + '''<h2>pages<h2/>'''
    return HttpResponse(response)


def profile(request, name, mobile):
    context = {'name': name, 'mobile': mobile}
    return render(request, 'myapp/profile.html', context)

def employee(request):
    name = ['Karthi', 'Kumar', 'Shiva']
    mobile = [9786910190, 912345678, 987654321]
    emp = zip(name, mobile)
    context = {'emp': emp}
    return render(request,'myapp/employee.html',context)


# name = ['Karthi', 'Kumar', 'Shiva']
# mobile = [9786910190, 912345678, 987654321]
# for i in name:
#     for j in mobile:
#         if name.index(i) == mobile.index(j):
#             print(i, j)
#
#
# name = ['Karthi', 'Kumar', 'Shiva']
# mobile = [9786910190, 912345678, 987654321]
# emp = zip(name,mobile)
# for i in emp:
#     print(i)

class Home(View):
    def get(self, request):
        return HttpResponse('Welcome to Class View of my Home')


class Employee(View):
        def get(self, request):
            name = ['Karthi', 'Kumar', 'Shiva']
            mobile = [9786910190, 912345678, 987654321]
            emp = zip(name, mobile)
            context = {'emp': emp}
            return render(request, 'myapp/employee.html', context)


class Swap(View):
    def get(self, request, home):
        context = {'home':home}
        return render(request,'myapp/home.html', context )





