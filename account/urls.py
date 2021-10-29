from django.urls import path
from .views import (
    Login_User,
    Logout_User,
    Register_User,
    HomeAdminView,
    ProfileAdminView,
    del_user,
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
    path('admin-panel/',HomeAdminView.as_view(),name='home'),
    path('admin-panel/create/',CreateArticleAdminView.as_view(),name='create_article'),
    path('admin-panel/update/<int:pk>',UpdateArticleAdminView.as_view(),name='update_article'),
    path('admin-panel/delete/<int:pk>',DeleteArticleAdminView.as_view(),name='delete_article'),
    path('admin-panel/users',UsersNumberAdminView.as_view(),name='users'),
    path('admin-panel/delete-user/<slug:username>',del_user,name='delete-user'),
    

]