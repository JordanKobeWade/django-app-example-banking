from django.shortcuts import render, redirect
from accounts.models import (Profile, Savings, Checking,
    MoneyMarket, CertificateDeposit, CertificateDepositIRA)
from accounts.forms import CustomUserCreationForm
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You may now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


