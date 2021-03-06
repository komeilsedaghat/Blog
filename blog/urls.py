from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('django.contrib.auth.urls')),
    path('',include('post.urls',namespace='posts')),
    path('account/',include('account.urls',namespace='account')),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
