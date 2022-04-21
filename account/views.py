from django.views.generic.detail import DetailView
from .models import User
from django.contrib.auth.views import LoginView,LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (LoginRequiredMixin)
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from post.models import Post
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from django.views import View
from .mixins import (
    AccessMixin,
    FormValidSaveMixin,
    SuperUserAccessMixin,
    StatusAuthorAccessMixin,
    SuperUserAuthorAccessMixin,
)
from django.views.generic import( 
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from .froms import (
    LoginUserForm,
    ProfileForm,
    RegisterUserForm,
)


class LoginUserView(SuccessMessageMixin,LoginView):
    template_name = 'account/Login.html'
    form_class = LoginUserForm
    success_message = 'You Logined Successfully'

class RegisterUserView(SuccessMessageMixin,CreateView):
    template_name = 'account/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('account:login')
    success_message = 'You Registered Successfully'


#logout view
class LogoutUserView(SuccessMessageMixin,LogoutView):
    success_message = 'You Logouted SuccessFully'


#Profile users
class ProfileAdminView(LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    model = User
    template_name = "admin-panel/profile.html"
    form_class = ProfileForm
    success_url = reverse_lazy('account:profile')
    success_message = "Your profile successfully Changed"
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
    fields= ["author","title","slug","category","description","image","status","is_special_article"]
    template_name = 'admin-panel/create_update.html'

    
#Update Article
class UpdateArticleAdminView(FormValidSaveMixin,StatusAuthorAccessMixin,AccessMixin,UpdateView):
    model = Post
    fields= ["author","title","slug","category","description","image","status","is_special_article"]
    template_name = 'admin-panel/create_update.html'
  

#Delete Article
class DeleteArticleAdminView(SuperUserAuthorAccessMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('account:home')
    template_name = 'admin-panel/confrim_delete_article.html'




class PreviewAdminView(LoginRequiredMixin,AccessMixin,DetailView):
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post,pk = pk)
    template_name = "post/detail.html"




class UsersNumberAdminView(LoginRequiredMixin,SuperUserAccessMixin,ListView):
    queryset = User.objects.all()
    template_name = 'admin-panel/user.html'

    def get_context_data(self,**kwargs):
        len_users = self.queryset.count()
        print(len_users)
        context = super().get_context_data(**kwargs)
        context['len_users'] = len_users
        return context


#Delete User
class DeleteUserView(LoginRequiredMixin,SuperUserAccessMixin,DeleteView):
    model = User
    success_url = reverse_lazy('account:users')
    slug_field = 'username'
    slug_url_kwarg = 'username'