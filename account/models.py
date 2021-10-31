from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    is_author = models.BooleanField(default=False,verbose_name="User is author?")
    is_special = models.DateTimeField(default=timezone.now,verbose_name="Special User")

    def is_special_user(self):
        if self.is_special > timezone.now():
            return True
        else:
            return False

    is_special_user.boolean = True