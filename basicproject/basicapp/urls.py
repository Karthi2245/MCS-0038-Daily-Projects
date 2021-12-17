#from django.contrib import admin
from django.urls import path
# We have to import the views module
#from . import views
from .views import *
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('basic/', my_fun),
    path('template/', my_template),
    path('temp/<str:page>', my_temp),
    path('profile/<str:name>,<int:mobile>', profile)

]
