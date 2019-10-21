from django.shortcuts import render, redirect
from accounts.models import (Profile, Savings, Checking,
    MoneyMarket, CertificateDeposit, CertificateDepositIRA)
from accounts.forms import CustomUserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
User = get_user_model()

def register(request):
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Account created! You may now login.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def dashboard(request):
    if request.user.is_authenticated:
        username = request.user.username
        user = User.objects.get(username=username)
        profile = Profile.objects.get(user=user)

        try:
            savings = Savings.objects.get(profile=profile)
        except ObjectDoesNotExist:
            savings = None

        try:
            checking = Checking.objects.get(profile=profile)
        except ObjectDoesNotExist:
            checking = None

        try:
            moneymarket = MoneyMarket.objects.get(profile=profile)
        except ObjectDoesNotExist:
            moneymarket = None
        
        try:
            cd = CertificateDeposit.objects.get(profile=profile)
        except ObjectDoesNotExist:
            cd = None

        try:
            cdira = CertificateDepositIRA.objects.get(profile=profile)
        except ObjectDoesNotExist:
            cdira = None

        context = {'savings': savings,
         'checking': checking,
         'moneymarket': moneymarket,
         'cd': cd,
         'cdira': cdira,
         }

        return render(request, 'dashboard.html', context=context)

    return render(request, 'dashboard.html')

def setup(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = ProfileForm(request.POST)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
                messages.success(request, 'Profile complete!')

                return redirect('dashboard')

        else:
            try:
                profile = Profile.objects.get(user=request.user)
            except ObjectDoesNotExist:
                profile = None
            
            if profile:
                return redirect('dashboard')
            else:
                form = ProfileForm()
                return render(request, 'setup.html', {'form': form})

    else:
        return render(request, 'pleaselogin.html')
    