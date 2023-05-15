from django.db import models
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class CustomUser(AbstractBaseUser):
    email=models.EmailField()
    phno=models.IntegerField()
    address=models.CharField(max_length=30)

