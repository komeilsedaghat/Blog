from django import forms
from django.db.models import fields
from .models import User
from django.http import request
from django.urls import reverse_lazy
from django.contrib import auth
from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.contrib.auth import authenticate, login ,logout
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib import messages
from .mixins import (
    AccessMixin,
    FormValidSaveMixin,
    StatusAuthorAccessMixin,
    SuperUserAuthorAccessMixin,
)
from post.models import Post
from django.views.generic import( 
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .froms import (
    LoginForm,
    ProfileForm,
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
                if request.user.is_superuser or request.user.is_author:
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


#Profile users
class ProfileAdminView(UpdateView):
    model = User
    template_name = "admin-panel/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(pk = self.request.user.pk)


#ADMIN PANEL VIEWS
#Home
class HomeAdminView(LoginRequiredMixin,AccessMixin,ListView):
    template_name = 'admin-panel/home.html'
    def get_queryset(self):
        return Post.objects.all()


#Add Article
class CreateArticleAdminView(LoginRequiredMixin,FormValidSaveMixin,StatusAuthorAccessMixin,AccessMixin,CreateView):
    model = Post
    fields= ["author","title","slug","category","description","image","status"]
    template_name = 'admin-panel/create_update.html'

    
#Update Article
class UpdateArticleAdminView(FormValidSaveMixin,StatusAuthorAccessMixin,AccessMixin,UpdateView):
    model = Post
    fields= ["author","title","slug","category","description","image","status"]
    template_name = 'admin-panel/create_update.html'
  

#Delete Article
class DeleteArticleAdminView(SuperUserAuthorAccessMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('account:home')
    template_name = 'admin-panel/confrim_delete.html'


