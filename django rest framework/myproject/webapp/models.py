from django.db import models

# Create your models here.


class Employee(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    emp_id = models.IntegerField()

    def __str__(self):
        # which is a string representation which return the all fields
        return self.first_name

























