from django.db import models
import re
import bcrypt
from datetime import datetime
from pytz import timezone

class UserManager(models.Manager):
    def registration_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['first_name']) < 2:
            errors["first_name"] = "first name should be at least 2 characters"
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last Name should be at least 2 characters"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):    # test whether a field matches the pattern            
            errors['email'] = ("Invalid email address!")
        if len(postData['password']) < 8:
            errors["password_len"] = "Password should be at least 8 characters"
        if len(User.objects.filter(email=postData['email']))>0:
            errors['email'] = ("email address exists!")
        if(postData['password']!=postData['confirm_pw']):
            errors['password'] = ("Passwords don't match")
        return errors
    
    def login_validator(self, postData):
        errors = {}
        user = User.objects.filter(email=postData['email'])
        if user:
            logged_user = user[0]
            print('login 1')
            if not bcrypt.checkpw(postData['password'].encode(), logged_user.password.encode()):
                print('login 2')
                errors['password'] = ("Incorrect Password")
        else:
            errors['user_details'] = ("Invalid data")
        return errors

    
# Create your models here.
class User(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.EmailField()
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()



