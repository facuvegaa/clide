from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
  is_client = models.BooleanField('client status', default=False)
  is_seller = models.BooleanField('seller status', default=False)
  email = models.EmailField(unique=True)

  def __str__(self):
     return self.username

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
     return self.username


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True) 
    company_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.company_name