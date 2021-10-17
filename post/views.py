from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class PostView(ListView):
    model = Post
    queryset = Post.objects.active_post()
    template_name = 'post/post.html'
    paginate_by = 2