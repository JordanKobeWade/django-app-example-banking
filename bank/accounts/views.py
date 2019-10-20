from django.shortcuts import render
from accounts.models import (Profile, Savings, Checking,
    MoneyMarket, CertificateDeposit, CertificateDepositIRA)

def index(request):
    return render(request, 'index.html')


