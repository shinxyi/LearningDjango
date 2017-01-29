from __future__ import unicode_literals
from django.db import models
import re, bcrypt
from time import gmtime, strftime
from django.core import serializers
#Our new manager!
#No methods in our new manager should ever catch the whole request object with a parameter!!! (just parts, like request.POST)
class UserManager(models.Manager):
    def register(self, first_name, last_name, email, birthday, password, confirm_password):
        valid = True
        errors = []
        pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(first_name) < 2 or len(last_name) < 2:
            errors.append("Name (First and Last) cannot be less than 2 characters!")
            valid=False
        elif first_name.isalpha() == False or last_name.isalpha() == False:
            errors.append("Name (First or Last) can only contain letters!")
            valid=False

        if len(email) < 1:
            errors.append("Email field cannot be empty!")
            validation=False
        elif not pattern.match(email):
            errors.append("Invalid Email Format!")
            valid=False

        if birthday >= str(strftime("%Y-%m-%d", gmtime())):
            errors.append("You must be at least a day old to register! Please check your birthday!")
            valid=False

        if len(password)<8:
            errors.append("Password must contain at least 8 characters!!")
            valid=False
        elif password != confirm_password:
            errors.append("Passwords do not match!!")
            valid=False

        if valid==True:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': pw_hash,
                'birthday': birthday
            }

            return {'user': user}

        return {'errors': errors }

    def login(self, email, password):
        valid=True
        errors=[]
        pattern = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        if len(email) < 1:
            errors.append("Email field cannot be empty!")
            valid=False
        elif not pattern.match(email):
            errors.append("Invalid Email Format!")
            valid=False

        user = User.userManager.filter(email=email)
        if len(user)<1:
            errors.append("Invalid Email")
            valid=False
        elif bcrypt.hashpw(password.encode(), user[0].password.encode()) == user[0].password.encode():
            return {'user': user[0]}
        return {'errors': errors }

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    birthday = models.DateField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    # *************************
    # Connect an instance of UserManager to our User model overwriting
    # the old hidden objects key with a new one with extra properties!!!
    userManager = UserManager()

    # *************************
