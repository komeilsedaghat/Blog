from django.urls import path
from .views import (
    Login_User,
    Logout_User,
    Register_User,
    HomeAdminView,
    ProfileAdminView,
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

]