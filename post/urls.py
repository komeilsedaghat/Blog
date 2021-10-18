from django.urls import path
from .views import (
    PostView,
    DetailView,
)

app_name = 'posts'
urlpatterns = [
    path('',PostView.as_view(),name = 'post'),
    path('page/<int:page>',PostView.as_view(),name = 'post'),
    path('detail/<int:pk>',DetailView.as_view(),name='detail'),
]