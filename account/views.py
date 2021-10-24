from django import forms
from .models import User
from django.http import request
from django.contrib import auth
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.contrib.auth import login
from django.contrib import messages
from .mixins import AccessMixin
from post.models import Post
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
                if request.user.is_superuser:
                    return redirect('account:home')
                else:
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
            User.objects.create_user(cd['username'],cd['email'],cd['password'])
            messages.success(request,"You registred successfully")
            return redirect('account:login')
    else:
        form = RegisterForm()
    return render(request,'account/register.html',{'form':form})


#logout view
def Logout_User(request):
    logout(request)
    messages.success(request,'You logouted successfully!')
    return redirect('posts:post')


#ADMIN PANEL VIEWS
class HomeAdminView(LoginRequiredMixin,AccessMixin,ListView):
    template_name = 'admin-panel/home.html'

    def get_queryset(self):
        return Post.objects.all()