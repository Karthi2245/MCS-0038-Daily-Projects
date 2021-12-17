from django.shortcuts import render
from django.http import *
from .models import Todolistitem
# from django.http import *


def todoappview(request):
    all_todo_items = Todolistitem.objects.all()
    return render(request, 'todolist.html',
                  {'all_items': all_todo_items})
    #return HttpResponse('')


# def addtodoview(request):
#     x = request.POST['content']
#     new_item = Todolistitem(content = x)
#     new_item.save()
#     return HttpResponseRedirect('/todoapp/')
#
#
# def deletetodoview(request, i):
#     y = Todolistitem.objects.get(id= i)
#     y.delete()
#     return HttpResponseRedirect('/todoapp/')

