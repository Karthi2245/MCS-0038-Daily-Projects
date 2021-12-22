from django.contrib import admin
from django.urls import path
from.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('info/', my_info),
    path('profile/', profile, name='np'),
]
