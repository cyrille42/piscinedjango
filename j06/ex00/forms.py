from django import forms
from django.contrib.auth.models import User
from .models import Tip

class RegisterForm(forms.ModelForm):

    confirm_password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        # password = forms.CharField(widget=forms.PasswordInput)
        model = User
        fields = ('username', 'password', )
        widgets = {
        	'password' : forms.PasswordInput(),
        }

class LoginForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = User
        fields = ('username', 'password',)
        widgets = {
        	'password' : forms.PasswordInput(),
        }

class TipForm(forms.ModelForm):

    class Meta:
        model = Tip
        fields = ('texte',)

