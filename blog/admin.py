from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'featured', 'status', 'created')
    list_editable = ('status', 'featured')
    list_filter = ('status', 'featured')
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    list_display_links = ('id', 'title')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.site_header = "AHISKA.NET - Yönetim"
admin.site.site_title = "AHISKA.NET - Ahıska Türkleri'nin Sesi"
admin.site.index_title = "Yönetim Paneli"
