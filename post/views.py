from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post


class PostView(ListView):
    queryset = Post.objects.active_post()
    template_name = 'post/post.html'
    paginate_by = 2


class DetailView(DetailView):
    template_name = 'post/detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post,pk = pk)
        