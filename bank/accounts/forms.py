from django import forms
from accounts.models import CustomUser
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
