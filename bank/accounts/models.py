from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=40)
    zip_code = models.CharField(max_length=9)
    birth_date = models.DateTimeField()

    def __str__(self):
        return self.user.username

class Document(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    one = models.FileField()
    one_description = models.CharField(max_length=25)
    two = models.FileField()
    two_description = models.CharField(max_length=25)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.profile.user.username

class Savings(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "savings"

    def __str__(self):
        return self.profile.user.username
    
class Checking(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.profile.user.username
    
class MoneyMarket(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.profile.user.username
    
class CertificateDeposit(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "CDs"

    def __str__(self):
        return self.profile.user.username
    
class CertificateDepositIRA(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    creation_date = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "IRA CDs"

    def __str__(self):
        return self.profile.user.username
    
class Deposit(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    account = models.CharField(max_length=25)
    amount = models.DecimalField(default=0, max_digits=9, decimal_places=2)
    deposit_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.profile.user.username


