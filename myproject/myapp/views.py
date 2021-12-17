from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# class based based view
# function based view

def index(request):
    return HttpResponse('Hello Harsha')

def name(request):
    response = """<p> Hi harsha you are in name</p>"""
    return HttpResponse(response)

def game(request, guess):
    response = """<h1> Hi harsha you are in this page number """ + guess +"""</h1>"""
    return HttpResponse(response)
# first we need to create a view
# we neet to create a route in urls.py
# need to add that route in proj urls.py

# urls --> views --> check data base if we need to store data or retrive
# send data to html --> that file is viewed

# from url we got ynamic --> urls.py --> view.py --> function --> we are accessing
# --> we will process an sen back to fe


def html_route(request):
    return render(request, 'myapp/index.html')
#path('harsha/<int: number>
def html_route2(request):
    context = {'number': 7904134297, 'sim':'jio'}
    return render(request,'myapp/main.html', context)

def html_route3(request):
    names = ['harsha','vardhan','ranjith']
    numbers = [ 2]
    context = {'names':names,'numbers': numbers}
    return render(request, 'myapp/number.html', context)