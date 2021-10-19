from django.urls import path
from .views import (
    PostView,
    DetailView,
    CategoryView,
)

app_name = 'posts'
urlpatterns = [
    path('',PostView.as_view(),name = 'post'),
    path('page/<int:page>',PostView.as_view(),name = 'post'),
    path('category/<slug:slug>',CategoryView.as_view(),name = 'category'),
    path('category/<slug:slug>/<int:page>',CategoryView.as_view(),name = 'category'),
    path('detail/<int:pk>',DetailView.as_view(),name='detail'),
]