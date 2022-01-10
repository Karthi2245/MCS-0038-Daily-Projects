from django.contrib import admin
from .models import Employee

# here i can add and delete my employees from the admin panel so
# i imported the models
# Register your models here.

admin.site.register(Employee)
