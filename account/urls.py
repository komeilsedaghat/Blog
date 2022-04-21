from django.urls import path
from django.contrib.auth import views

from . import views

app_name ='account'
urlpatterns = [
    path('login/',views.LoginUserView.as_view(),name='login'),
    path('register/',views.RegisterUserView.as_view(),name='register'),
    path('logout/',views.LogoutUserView.as_view(),name='logout'),
    path('profile/',views.ProfileAdminView.as_view(),name='profile'),
    path('admin-panel/',views.HomeAdminView.as_view(),name='home'),
    path('admin-panel/create/',views.CreateArticleAdminView.as_view(),name='create_article'),
    path('admin-panel/update/<int:pk>',views.UpdateArticleAdminView.as_view(),name='update_article'),
    path('admin-panel/delete/<int:pk>',views.DeleteArticleAdminView.as_view(),name='delete_article'),
    path('admin-panel/users/',views.UsersNumberAdminView.as_view(),name='users'),
    path('admin-panel/users/delete/<str:username>/',views.DeleteUserView.as_view(),name='delete_user'),
    path('admin-panel/preview/<int:pk>/',views.PreviewAdminView.as_view(),name='preview'),
]