from django.db import models
from django.utils.html import format_html
from account.models import User


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
    description = models.TextField()
    author  = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to = 'media')
    created = models.DateTimeField(auto_now_add=True)
    status= models.CharField(max_length=1,choices=STATUS)
    objects = ManagerPost()

    def __str__(self):
        return self.title

    def image_show(self):
        return format_html("<img width=100 height = 84 style = 'border-radius:20px;' src='{}'> ".format(self.image.url))


    def description_shorter(self):
        des = self.description[:60] + '...'
        return des