from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Details


# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        obj = Details.objects.create(name=name, age=age, address=address)
    obj.save()
    return redirect('/')