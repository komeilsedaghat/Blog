from django.urls import path
from .views import (
    Login_User,
    Logout_User,
    Register_User,
    HomeAdminView,
)

app_name = 'account'
urlpatterns = [
    path('login/',Login_User,name='login'),
    path('register/',Register_User,name='register'),
    path('logout/',Logout_User,name='logout'),
    path('admin-panel/',HomeAdminView.as_view(),name='home')
]