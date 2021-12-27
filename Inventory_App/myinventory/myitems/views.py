from django.shortcuts import *
from .models import *

# Create your views here.


def items(request):
    all_items = Inventory.objects.all()
    return render(request, 'myitems/items.html', {'add_items': all_items})


def add_items(request):
    x = request.POST['add_items']
    new_item = Inventory(add_items=x)
    new_item.save()
    return HttpResponseRedirect('items')

def grocery_items(request):
    return render(request, 'myitems/list_grocery.html')



