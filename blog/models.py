from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Kategori')
    slug = models.SlugField(max_length=50, unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Açıklama')

    class Meta:
        verbose_name = "Kategori"
        verbose_name_plural = "Kategoriler"

    def get_absolute_url(self):
        return reverse('list_by_category', kwargs={'slug': self.slug})

    def __str__(self):
        return self.name

# STATUS = (
#    (0,"Pasif"),
#    (1,"Aktif")
# )

class Article(models.Model):
    title = models.CharField(max_length=100, unique=True, verbose_name='Başlık')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='URL')
    description = models.CharField(max_length=255, verbose_name='Özet')
    content = RichTextField(blank=True,null=True, verbose_name='İçerik')
    image = models.ImageField(upload_to="upload/article/images/%Y/%m/%d/", verbose_name='Resim')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Kategori')
    tags = TaggableManager(verbose_name='Etiket')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Yazar')
    # status = models.IntegerField(choices=STATUS, default=0, verbose_name='Yayın Durumu')
    status = models.BooleanField(default=False, verbose_name='Yayında')
    featured = models.BooleanField(default=False, verbose_name='Manşet')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Tarih')
    updated = models.DateTimeField(auto_now=True, verbose_name='Güncelleme')

    class Meta:
        ordering = ['-created']
        verbose_name = "Haber"
        verbose_name_plural = "Haberler"

    def get_absolute_url(self):
        return reverse('article_detail', kwargs={'slug': self.slug, 'pk': self.pk}) # haber/id/slug şeklinde olması için

    def __str__(self):
        return self.title
