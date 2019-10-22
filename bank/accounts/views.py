from django.shortcuts import render, redirect
from accounts.models import (Profile, Savings, Checking, Document,
    MoneyMarket, CertificateDeposit, CertificateDepositIRA)
from accounts.forms import CustomUserCreationForm, ProfileForm, UploadForm
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
User = get_user_model()

def index(request):
    if not request.user.is_authenticated:
        return redirect('login')
    else:
        return redirect('dashboard')

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
        user = request.user

        try:
            profile = Profile.objects.get(user=user)
        except ObjectDoesNotExist:
            return redirect('setup')

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

        if ((savings == None) and (checking == None) and 
            (moneymarket == None) and (cd == None) and (cdira == None)):
            return redirect('products')

        context = {'savings': savings,
         'checking': checking,
         'moneymarket': moneymarket,
         'cd': cd,
         'cdira': cdira,
         }

        return render(request, 'dashboard.html', context=context)

    return redirect('error')

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
        return redirect('error')
    
def products(request):
    if request.user.is_authenticated:
        return render(request, 'products.html')
    else:
        return redirect('error')

def profile(request):
    if request.user.is_authenticated:
        username = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        profile = Profile.objects.get(user=request.user)
        street_address = profile.street_address
        city = profile.city
        zip_code = profile.zip_code
        birth_date = profile.birth_date
        try:
            document = Document.objects.get(profile=profile)
        except ObjectDoesNotExist:
            document = None
        
        if document:
            document_status = document.accepted
        else:
            document_status = None

        if document:
            if document_status == True:
                document_status = 'Approved'
            else:
                document_status = 'Processing'
        else:
            document_status = 'No submissions'
        
        context = {'username':username,
            'first_name':first_name,
            'last_name':last_name,
            'street_address':street_address,
            'birth_date':birth_date,
            'document_status':document_status,
            'email':email,
            'city':city,
            'zip_code':zip_code,
            }

        return render(request, 'profile.html', context)
    else:
        return redirect('error')

def document_uploader(request):
    if request.user.is_authenticated:
        if request.method =='POST':
            form = UploadForm(request.POST, request.FILES)

            if form.is_valid():
                instance = form.save(commit=False)
                instance.profile = Profile.objects.get(user=request.user)
                instance.save()
                messages.success(request, 'Document upload successful!')
                return redirect('dashboard')

        else:
            profile = Profile.objects.get(user=request.user)
        
            try:
                document = Document.objects.get(profile=profile)
            except ObjectDoesNotExist:
                document = None

            if document:
                messages.warning(request, 'You already submitted your documents')
                return redirect('profile')
            else:
                form = UploadForm()
        return render(request, 'upload.html', {'form': form})
    else:
        return redirect('error')

def savings_page(request):
    if request.user.is_authenticated:
        return render(request, 'product/savings.html')
    else:
        return redirect('error')


def checking_page(request):
    if request.user.is_authenticated:
        return render(request, 'product/checking.html')
    else:
        return redirect('error')

def moneymarket_page(request):
    if request.user.is_authenticated:
        return render(request, 'product/moneymarket.html')
    else:
        return redirect('error')

def cd_page(request):
    if request.user.is_authenticated:
        return render(request, 'product/cd.html')
    else:
        return redirect('error')

def iracd_page(request):
    if request.user.is_authenticated:
        return render(request, 'product/iracd.html')
    else:
        return redirect('error')

def please_login(request):
    return render(request, 'pleaselogin.html')
