from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.ModelForm):

    class Meta:
        password = forms.CharField(widget=forms.PasswordInput)
        model = User
        fields = ('username', 'password',)
        widgets = {
        	'password' : forms.PasswordInput(),
        }