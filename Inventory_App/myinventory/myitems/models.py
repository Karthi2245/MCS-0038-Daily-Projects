from django.db import models

# Create your models here.

class Inventory(models.Model):
    grocery_items = models.TextField(50)
    electronic_items = models.TextField(50)
    clothing_items = models.TextField(50)
    add_items = models.TextField(50)

