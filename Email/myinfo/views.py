from django.shortcuts import *
from django.contrib.auth import authenticate, login # For authentication
from django.contrib.auth.models import User  # For getting user input


# Create your views here.


def my_info(request):
    if request.method == 'POST':


        search_query = request.POST('user', None)
        return render(request, 'myinfo/profile.html')
    return render(request, "myinfo/info.html", request.POST)


# def profile(request):
#     if request.method == 'GET':
#         search_query = request.GET.get('user', None)
#         return render(request, 'myinfo/profile.html', locals())

def profile(request):

    return render(request, 'myinfo/profile.html')
