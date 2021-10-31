from django.urls import path
from django.contrib.auth import views
from .views import (
    Login_User,
    Logout_User,
    Register_User,
    del_user,
    HomeAdminView,
    ProfileAdminView,
    PreviewAdminView,
    PasswordChange,
    PasswordChangeDone,
    UsersNumberAdminView,
    CreateArticleAdminView,
    UpdateArticleAdminView,
    DeleteArticleAdminView,
)

app_name = 'account'
urlpatterns = [
    path('login/',Login_User,name='login'),
    path('register/',Register_User,name='register'),
    path('logout/',Logout_User,name='logout'),
    path('profile/',ProfileAdminView.as_view(),name='profile'),
    path('profile/password_change/', PasswordChange.as_view(), name='password_change'),
    path('profile/password_change/done/', PasswordChangeDone.as_view(), name='password_change_done'),
    path('admin-panel/',HomeAdminView.as_view(),name='home'),
    path('admin-panel/create/',CreateArticleAdminView.as_view(),name='create_article'),
    path('admin-panel/update/<int:pk>',UpdateArticleAdminView.as_view(),name='update_article'),
    path('admin-panel/delete/<int:pk>',DeleteArticleAdminView.as_view(),name='delete_article'),
    path('admin-panel/users',UsersNumberAdminView.as_view(),name='users'),
    path('admin-panel/delete-user/<slug:username>',del_user,name='delete-user'),
    path('admin-panel/preview/<int:pk>/',PreviewAdminView.as_view(),name='preview'),


    

]