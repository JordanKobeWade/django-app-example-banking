from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    zipcode = models.CharField(max_length=9)
    birthdate = models.DateTimeField(default=timezone.now)
    document = models.FileField(upload_to='uploads/')

class Savings(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=500, max_digits=9, decimal_places=2)

class Checking(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=500, max_digits=9, decimal_places=2)

class MoneyMarket(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=10000, max_digits=9, decimal_places=2)

class CertificateDeposit(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=1000, max_digits=9, decimal_places=2)

class CertificateDepositIRA(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)
    minimum = models.DecimalField(default=1000, max_digits=9, decimal_places=2)



