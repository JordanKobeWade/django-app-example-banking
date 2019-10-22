from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from accounts.models import (CustomUser, Profile, Document,
    Savings, Checking, MoneyMarket, CertificateDeposit,
    CertificateDepositIRA, Deposit)
from accounts.forms import (CustomUserCreationForm, 
    CustomUserChangeForm)

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Document)
admin.site.register(Savings)
admin.site.register(Checking)
admin.site.register(MoneyMarket)
admin.site.register(CertificateDeposit)
admin.site.register(CertificateDepositIRA)
admin.site.register(Deposit)



