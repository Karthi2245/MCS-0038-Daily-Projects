from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', todoappview ),
    path('save/', addtodoview),
    path('delete/<int:i>', deletetodoview)
]


