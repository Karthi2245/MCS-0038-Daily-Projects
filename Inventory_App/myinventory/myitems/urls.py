from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('items',items),
    path('it', add_items),
    path('grocery', grocery_items),
]
