from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.TextField(max_length=20)
    password = models.CharField(('password'), max_length=128)

