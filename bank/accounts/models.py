from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    
class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=9)
    birthdate = models.DateTimeField(default=timezone.now)
    document = models.FileField(upload_to='uploads/')

class Savings(models.Model):
    status_types = ('inactive', 'processing', 'active')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=500, max_digits=9, decimal_places=2)
    status = models.CharField(max_length=10, default=status_types[0])

class Checking(models.Model):
    status_types = ('inactive', 'processing', 'active')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=500, max_digits=9, decimal_places=2)
    status = models.CharField(max_length=10, default=status_types[0])

class MoneyMarket(models.Model):
    status_types = ('inactive', 'processing', 'active')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=10000, max_digits=9, decimal_places=2)
    status = models.CharField(max_length=10, default=status_types[0])

class CertificateDeposit(models.Model):
    status_types = ('inactive', 'processing', 'active')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=1000, max_digits=9, decimal_places=2)
    status = models.CharField(max_length=10, default=status_types[0])

class CertificateDepositIRA(models.Model):
    status_types = ('inactive', 'processing', 'active')
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=1000, max_digits=9, decimal_places=2)
    status = models.CharField(max_length=10, default=status_types[0])



