from __future__ import unicode_literals
from django import forms
from django.core.exceptions import ValidationError
from django.db import models
import re, bcrypt


class UserManager(models.Manager):
    def register(self, first_name, last_name, email, password, confirm_password):
        if password == confirm_password:
            pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'password': pw_hash
            }

            return {'user': user}

        return {'error': 'Passwords do not match!'}

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

# our validator
def validateLengthGreaterThanTwo(value):
    if len(value)< 3:
        raise ValidationError(
          '{} must be longer than 2 characters'.format(value)
          )
def validateLengthGreaterThanEight(value):
    if len(value)< 8:
        raise ValidationError(
          '{} must be longer than 8 characters'.format(value)
          )
def isAlpha(value):
    if not value.isalpha():
        raise ValidationError(
          '{} can only contain letters'.format(value)
          )

class User(models.Model):
    first_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo, isAlpha])
    last_name = models.CharField(max_length=45, validators = [validateLengthGreaterThanTwo, isAlpha])
    email = models.EmailField()
    password=models.CharField(max_length=100, validators = [validateLengthGreaterThanEight])
    confirm_password=models.CharField(max_length=100)

    userManager = UserManager()
