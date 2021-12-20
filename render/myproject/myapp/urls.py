from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myfun/', my_fun),
    path('temp1/', my_template),
    path('temp2/<str:page>', my_temp),
    path('details/<str:name>,<int:mobile>', profile),
    path('employee/', employee),
    path('emp/', Employee.as_view(), name ='Employee Details' ),
    path('emp1/', Employee.as_view(), name='Employee Details'),
    path('home/<str:home>', Swap.as_view(), name='Employee Details'),

]
