from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Category


def blog(request):
    articles = Article.objects.filter(status=1).order_by('-created_date')
    tags = Tag.objects.order_by('content')
    context = {'articles': articles, 'tab_name': 'Blog', 'tags' : tags}
    return render(request, 'blog.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article.html', {'article': article})

def tag(request, tag_id):
    articles = Article.objects.filter(tags=tag_id)
    tag = Tag.objects.get(id=tag_id)
    return render(request, 'tag.html', {'articles': articles, 'tag': tag})

def category(request, category_id):
    articles = Article.objects.filter(category=category_id)
    return render(request, 'tag.html', {'articles': articles})

def tags(request):
    items = Tag.objects.all()
    return render(request, 'tags_categories.html', {'param': items, 'name': 'Tags', 'url': 'tag'})

def categories(request):
    items = Category.objects.all()
    return render(request, 'tags_categories.html', {'param': items, 'name': 'Categories', 'url': 'tag'})

