from django.contrib import admin
from django.urls import path, include
from django.conf import settings #sonradan eklenen
from django.conf.urls.static import static #sonradan eklenen

urlpatterns = [
    path('', include('home.urls')),
    path('haber/', include('blog.urls')),
    path('iletisim/', include('contact.urls')),
    path('users/', include('users.urls')),
    path('admin/', admin.site.urls)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #sonradan eklenen