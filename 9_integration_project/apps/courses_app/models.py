from __future__ import unicode_literals

from django.db import models
from ..loginreg_app.models import User

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    students = models.ManyToManyField(User)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

class Description(models.Model):
    course = models.OneToOneField(Course)
    description = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
