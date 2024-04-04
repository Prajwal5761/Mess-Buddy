from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    breakfast_amt = models.IntegerField(default=0)
    plates = models.IntegerField(default=0)
    lunch_amt = models.IntegerField(default=0)

    def __str__(self):
        return self.user.username
    

