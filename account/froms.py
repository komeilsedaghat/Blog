from django import forms
from django.forms.forms import Form
from .models import User

#Login Form
class LoginForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Username'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'}))


#Register Form
class RegisterForm(forms.Form):
    username = forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Your Username'}))
    email    = forms.EmailField(max_length=40,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Your Email'}))
    password = forms.CharField(max_length=50,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Your Password'}))
   

    def clean_email(self):
        email = self.cleaned_data['email']
        user  = User.objects.filter(email = email)
        if user.exists():
            raise forms.ValidationError("this email is already exists")
        else:
            return email