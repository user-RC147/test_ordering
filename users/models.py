from os import name
from django.db import models
from django.contrib.auth.models import AbstractUser

from config import settings

# Create your models here.
class CustomUser(AbstractUser):
    name=models.CharField(max_length=50)
    data_create=models.DateTimeField(auto_now_add=True)