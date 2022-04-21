from django import forms
from django.forms import fields
from django.forms.forms import Form
from .models import User
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm


class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields= ('username','password',)

    def __init__(self,*args,**kwargs):
        super(LoginUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class':'input100','placeholder':'Your Username'}
        self.fields['password'].widget.attrs = {'class':'input100','placeholder':'Your Password'}


    

#Register Form
class RegisterUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ('username','email','password1','password2','first_name','last_name')


    def __init__(self,*args,**kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class':'input100','placeholder':'Your username'}
        self.fields['email'].widget.attrs = {'class':'input100','placeholder':'Your email'}
        self.fields['password1'].widget.attrs = {'class':'input100','placeholder':'Your Password'}
        self.fields['password2'].widget.attrs = {'class':'input100','placeholder':'Your Confirm Password'}
        self.fields['first_name'].widget.attrs = {'class':'input100','placeholder':'Your firstname'}
        self.fields['last_name'].widget.attrs = {'class':'input100','placeholder':'Your lastname'}


    


    def clean_email(self):
        email = self.cleaned_data['email']
        user  = User.objects.filter(email = email)
        if user.exists():
            raise forms.ValidationError("this email is already exists")
        else:
            return email


#ProfileForm
class ProfileForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)

        self.fields['username'].disabled = True
        self.fields['username'].help_text = None
        self.fields['email'].disabled = True
        self.fields['is_author'].disabled = True

    class Meta:
        model = User
        fields = [
            'username','email','first_name',
            'last_name','is_author',
        ]