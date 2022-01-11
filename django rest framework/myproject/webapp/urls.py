from django.urls import path
from .views import *

urlpatterns = [
    path('employee/', EmployeeList.as_view()),
    path('employee/<int:id>/', EmployeeDetail.as_view(),)

]
