from django.shortcuts import render
from django.http import HttpResponse

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
    context = {'name': name, 'sim': mobile}
    return render(request,'myapp/profile.html', context)




