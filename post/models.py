from django.db import models
from django.utils.html import format_html
from django.urls import reverse
from account.models import User


#Manager for Category
class ManageCategory(models.Manager):
    def active_category(self):
        return self.filter(status = True)


#Category model
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20)
    status = models.BooleanField(default=True)
    objects= ManageCategory()

    def __str__(self):
        return self.name



#manager post model
class ManagerPost(models.Manager):
    def active_post(self):
        return self.filter(status = 'p')


#post model
class Post(models.Model):
    STATUS = (
        ('p','publish'),
        ('d','draft'),
    )
    title = models.CharField(max_length=130)
    slug  = models.CharField(max_length=130)
    category= models.ManyToManyField(Category,related_name='articles')
    description = models.TextField()
    author  = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media')
    created = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=1,choices=STATUS)
    objects = ManagerPost()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['-created']

    def __str__(self): 
        return self.title

    def image_show(self):
        return format_html("<img width=100 height = 84 style = 'border-radius:20px;' src='{}'> ".format(self.image.url))
    image_show.short_description = "image"


    def description_shorter(self):
        des = self.description[:60] + '...'
        return des
    description_shorter.short_description = "body"


    def category_show(self):
        return ",".join([category.name for category in self.category.active_category()])
    category_show.short_description = "category"

    def get_absolute_url(self):
        return reverse('account:home')