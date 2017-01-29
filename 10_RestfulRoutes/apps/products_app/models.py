from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def checkProduct(self, name, description, price):
        valid = True
        errors = []

        if len(name) < 2:
            errors.append("Name cannot be less than 2 characters!")
            valid=False

        if len(description) < 1:
            errors.append("Description field cannot be empty!")
            valid=False

        if price<=0:
            errors.append("Price cannot be less than or equal to $0!")
            valid=False

        if valid==True:
            product = {
                'name': name,
                'description': description,
                'price': price
            }
            return {'product': product}

        return {'errors': errors }

class Product(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    objects = ProductManager()
