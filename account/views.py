from django import forms
from django.contrib import auth
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from .models import User
from .froms import (
    LoginForm,
    RegisterForm,
)



#login view
def Login_User(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'You Logined Successfully!')
                return redirect('posts:post')
            else:
                messages.error(request,'Your password or username is wrong!')
    else:
        form = LoginForm()
    return render(request,'account/Login.html',{'form':form})


#register view
def Register_User(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(cd['username'],cd['email'],cd['password'])
            login(request,user)
            messages.success(request,"You registred successfully")
            return redirect('posts:post')
    else:
        form = RegisterForm()
    return render(request,'account/register.html',{'form':form})


#logout view
def Logout_User(request):
    logout(request)
    messages.success(request,'You logouted successfully!')
    return redirect('posts:post')