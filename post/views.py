from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from .models import Post,Category


class PostView(ListView):
    queryset = Post.objects.active_post()
    template_name = 'post/post.html'
    paginate_by = 2


class DetailView(DetailView):
    template_name = 'post/detail.html'
    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Post,pk = pk)
        

class CategoryView(ListView):
    template_name = 'post/category.html'
    paginate_by = 2
    def get_queryset(self):
        global category
        slug = self.kwargs.get('slug')
        category = get_object_or_404(Category.objects.active_category(),slug=slug)
        return category.articles.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = category
        return context
 