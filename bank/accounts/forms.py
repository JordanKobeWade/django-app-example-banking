from django import forms
from django.forms import ModelForm
from accounts.models import CustomUser, Profile, Document, Deposit
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=80)
    last_name = forms.CharField(max_length=80)
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')

class ProfileForm(ModelForm):

    class Meta:
        model = Profile
        fields = ('street_address', 'city', 'zip_code', 'birth_date')

class UploadForm(ModelForm):

    class Meta:
        model = Document
        fields = ('one', 'one_description', 'two', 'two_description')

class DepositForm(ModelForm):

    class Meta:
        model = Deposit
        fields = ('amount',)

