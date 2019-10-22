from django.shortcuts import render, redirect
from accounts.models import (Profile, Savings, Checking, Document,
    MoneyMarket, CertificateDeposit, CertificateDepositIRA)
from accounts.forms import (CustomUserCreationForm, ProfileForm, 
    UploadForm, DepositForm)
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

        if savings:
            savings_status = "Active"
        else:
            savings_status = "Not Active"
        
        if checking:
            checking_status = "Active"
        else:
            checking_status = "Not Active"

        if moneymarket:
            mm_status = "Active"
        else:
            mm_status = "Not Active"

        if cd:
            cd_status = "Active"
        else:
            cd_status = "Not Active"

        if cdira:
            cdira_status = "Active"
        else:
            cdira_status = "Not Active"

        context = {'savings': savings,
         'checking': checking,
         'moneymarket': moneymarket,
         'cd': cd,
         'cdira': cdira,
         'savings_status': savings_status,
         'checking_status': checking_status,
         'mm_status': mm_status,
         'cd_status': cd_status,
         'cdira_status': cdira_status,
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

def open_savings(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        try:
            document = Document.objects.get(profile=profile)
        except ObjectDoesNotExist:
            document = None
        
        if document:
            if document.accepted != True:
                messages.warning(request, 'Documents are still being processed.')
                return redirect('savings')
            elif document.accepted == True:
                if request.method == 'POST':
                    form = DepositForm(request.POST)

                    if form.is_valid():
                        amount = form.cleaned_data.get('amount')
                        if amount >= 500:
                            instance = form.save(commit=False)
                            instance.profile = Profile.objects.get(user=request.user)
                            instance.account = 'savings'
                            instance.save()

                            created_account = Savings()
                            created_account.balance = amount
                            created_account.profile= Profile.objects.get(user=request.user)
                            created_account.save()

                            messages.success(request, 'Account Opened!')
                            return redirect('dashboard')
                        else:
                            messages.warning(request, 'Minimum deposit not met. Please try again.')
                            return redirect('savings')
                else:
                    profile = Profile.objects.get(user=request.user)

                    try:
                        savings = Savings.objects.get(profile=profile)
                    except ObjectDoesNotExist:
                        savings = None

                    if savings:
                        messages.warning(request, 'Account already exists.')
                        return redirect('dashboard')
                    else:
                        form = DepositForm()
                return render(request, 'product/opensavings.html', {'form': form})
        else:
            messages.warning(request, 'Please upload documents.')
            return redirect('upload')
    else:
        return redirect('error')

def open_checking(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        try:
            document = Document.objects.get(profile=profile)
        except ObjectDoesNotExist:
            document = None
        
        if document:
            if document.accepted != True:
                messages.warning(request, 'Documents are still being processed.')
                return redirect('checking')
            elif document.accepted == True:
                if request.method == 'POST':
                    form = DepositForm(request.POST)

                    if form.is_valid():
                        amount = form.cleaned_data.get('amount')
                        if amount >= 500:
                            instance = form.save(commit=False)
                            instance.profile = Profile.objects.get(user=request.user)
                            instance.account = 'checking'
                            instance.save()

                            created_account = Checking()
                            created_account.balance = amount
                            created_account.profile= Profile.objects.get(user=request.user)
                            created_account.save()

                            messages.success(request, 'Account Opened!')
                            return redirect('dashboard')
                        else:
                            messages.warning(request, 'Minimum deposit not met. Please try again.')
                            return redirect('checking')
                else:
                    profile = Profile.objects.get(user=request.user)

                    try:
                        checking = Checking.objects.get(profile=profile)
                    except ObjectDoesNotExist:
                        checking = None

                    if checking:
                        messages.warning(request, 'Account already exists.')
                        return redirect('dashboard')
                    else:
                        form = DepositForm()
                return render(request, 'product/openchecking.html', {'form': form})
        else:
            messages.warning(request, 'Please upload documents.')
            return redirect('upload')
    else:
        return redirect('error')


def open_moneymarket(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        try:
            document = Document.objects.get(profile=profile)
        except ObjectDoesNotExist:
            document = None
        
        if document:
            if document.accepted != True:
                messages.warning(request, 'Documents are still being processed.')
                return redirect('moneymarket')
            elif document.accepted == True:
                if request.method == 'POST':
                    form = DepositForm(request.POST)

                    if form.is_valid():
                        amount = form.cleaned_data.get('amount')
                        if amount >= 1000:
                            instance = form.save(commit=False)
                            instance.profile = Profile.objects.get(user=request.user)
                            instance.account = 'moneymarket'
                            instance.save()

                            created_account = MoneyMarket()
                            created_account.balance = amount
                            created_account.profile= Profile.objects.get(user=request.user)
                            created_account.save()

                            messages.success(request, 'Account Opened!')
                            return redirect('dashboard')
                        else:
                            messages.warning(request, 'Minimum deposit not met. Please try again.')
                            return redirect('moneymarket')
                else:
                    profile = Profile.objects.get(user=request.user)

                    try:
                        moneymarket = MoneyMarket.objects.get(profile=profile)
                    except ObjectDoesNotExist:
                        moneymarket = None

                    if moneymarket:
                        messages.warning(request, 'Account already exists.')
                        return redirect('dashboard')
                    else:
                        form = DepositForm()
                return render(request, 'product/openmoneymarket.html', {'form': form})
        else:
            messages.warning(request, 'Please upload documents.')
            return redirect('upload')
    else:
        return redirect('error')

def open_cd(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        try:
            document = Document.objects.get(profile=profile)
        except ObjectDoesNotExist:
            document = None
        
        if document:
            if document.accepted != True:
                messages.warning(request, 'Documents are still being processed.')
                return redirect('cd')
            elif document.accepted == True:
                if request.method == 'POST':
                    form = DepositForm(request.POST)

                    if form.is_valid():
                        amount = form.cleaned_data.get('amount')
                        if amount >= 10000:
                            instance = form.save(commit=False)
                            instance.profile = Profile.objects.get(user=request.user)
                            instance.account = 'cd'
                            instance.save()

                            created_account = CertificateDeposit()
                            created_account.balance = amount
                            created_account.profile= Profile.objects.get(user=request.user)
                            created_account.save()

                            messages.success(request, 'Account Opened!')
                            return redirect('dashboard')
                        else:
                            messages.warning(request, 'Minimum deposit not met. Please try again.')
                            return redirect('cd')
                else:
                    profile = Profile.objects.get(user=request.user)

                    try:
                        cd = CertificateDeposit.objects.get(profile=profile)
                    except ObjectDoesNotExist:
                        cd = None

                    if cd:
                        messages.warning(request, 'Account already exists.')
                        return redirect('dashboard')
                    else:
                        form = DepositForm()
                return render(request, 'product/opencd.html', {'form': form})
        else:
            messages.warning(request, 'Please upload documents.')
            return redirect('upload')
    else:
        return redirect('error')

def open_iracd(request):
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        try:
            document = Document.objects.get(profile=profile)
        except ObjectDoesNotExist:
            document = None
        
        if document:
            if document.accepted != True:
                messages.warning(request, 'Documents are still being processed.')
                return redirect('iracd')
            elif document.accepted == True:
                if request.method == 'POST':
                    form = DepositForm(request.POST)

                    if form.is_valid():
                        amount = form.cleaned_data.get('amount')
                        if amount >= 10000:
                            instance = form.save(commit=False)
                            instance.profile = Profile.objects.get(user=request.user)
                            instance.account = 'iracd'
                            instance.save()

                            created_account = CertificateDepositIRA()
                            created_account.balance = amount
                            created_account.profile= Profile.objects.get(user=request.user)
                            created_account.save()

                            messages.success(request, 'Account Opened!')
                            return redirect('dashboard')
                        else:
                            messages.warning(request, 'Minimum deposit not met. Please try again.')
                            return redirect('iracd')
                else:
                    profile = Profile.objects.get(user=request.user)

                    try:
                        iracd = CertificateDepositIRA.objects.get(profile=profile)
                    except ObjectDoesNotExist:
                        iracd = None

                    if iracd:
                        messages.warning(request, 'Account already exists.')
                        return redirect('dashboard')
                    else:
                        form = DepositForm()
                return render(request, 'product/openiracd.html', {'form': form})
        else:
            messages.warning(request, 'Please upload documents.')
            return redirect('upload')
    else:
        return redirect('error')