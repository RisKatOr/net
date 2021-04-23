from django.shortcuts import get_object_or_404, get_list_or_404
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Article, Category
from hitcount.views import HitCountDetailView
from taggit.models import Tag



class ArticleListView(ListView):
    model = Article
    paginate_by = 10
    queryset = Article.objects.filter(status=True)
    # template_name = 'blog/article_list.html' #<app>/<model>_<viewtype>.html
    # ordering = ['-created'] # Model'de Article'ın sıralaması zaten tarihe göre ayarlı olduğunda buna burada gerek yok yada farklı bir unsura göre sıralama olabilir
    # context_object_name = 'article_list' # Varsayılan olarak object_list ve modelAdı_list yani zaten article_list 'dir.

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')
        context['latest_list'] = get_list_or_404(Article, status=True)
        return context


class ArticleDetailView(HitCountDetailView):
    model = Article
    count_hit = True
    #context_object_name = 'article' # default <model>
    #template_name = 'blog/article_detail.html' # default <app>/<model>_<viewtype>.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['similar_articles'] = self.object.tags.similar_objects()
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')
        context['latest_list'] = get_list_or_404(Article, status=True)
        return context


class UserArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(status=True)
    template_name = 'blog/user_articles.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'user_articles'
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return super(UserArticleListView, self).get_queryset().filter(author=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.get(username__iexact=self.kwargs.get('username'))
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')
        context['latest_list'] = Article.objects.filter(status=True)
        return context


class CategoryArticleListView(ListView):
    model = Article
    queryset = Article.objects.filter(status=True)
    template_name = 'blog/category_posts.html'
    context_object_name = 'category_posts'
    paginate_by = 10
    # slug_url_kwarg = 'slug'

    def get_queryset(self):
        category = get_object_or_404(Category, slug=self.kwargs['slug'])
        return super(CategoryArticleListView, self).get_queryset().filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = Category.objects.get(slug__iexact=self.kwargs.get('slug'))
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')
        context['latest_list'] = Article.objects.filter(status=True)
        return context


class TagsListView(ListView):
    model = Tag
    template_name = 'blog/tags_list.html'
    context_object_name = 'tags_list'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')
        context['latest_list'] = Article.objects.filter(status=True)
        return context


class TagListView(ListView):
    model = Article
    template_name = 'blog/tag_list.html'
    context_object_name = 'tag_list'
    paginate_by = 10

    def get_queryset(self):
        tags = get_object_or_404(Tag, slug=self.kwargs['slug'])
        return super().get_queryset().filter(tags=tags)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag'] = Tag.objects.get(slug__iexact=self.kwargs.get('slug'))
        context['featured_list'] = Article.objects.filter(status=True, featured=True).order_by('?')
        context['latest_list'] = Article.objects.filter(status=True)
        return context
