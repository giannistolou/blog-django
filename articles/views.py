from landing.models import Landing_seo
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import Http404
from django.shortcuts import render, get_object_or_404
from .models import Article, Tag, Category
from django.core.paginator import Paginator

def blog(request, page_number = 1):
    articles_οbject = Article.objects.filter(status=1).order_by('-created_date')
    articles =  Paginator(articles_οbject, 5)
    tags = Tag.objects.order_by('content')
    try:
        seo = Landing_seo.objects.all()[0]
        print(seo)
    except:
        seo = []
    context = {'articles': articles.page(page_number), 'tab_name': 'Blog', 'name': 'Blog', 'tags' : tags, 'pagenation_link': '/blog', 'seo': seo}
    return render(request, 'blog.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    if(article.status != 1):
         raise Http404
    return render(request, 'article.html', {'article': article})

def tag(request, tag_id, page_number=1):
    articles_οbject = Article.objects.filter(tags=tag_id)
    articles =  Paginator(articles_οbject, 5)
    tag = Tag.objects.get(id=tag_id)
    pagenation_link = '/blog/tag/' + str(tag_id)
    return render(request, 'blog.html', {'articles': articles.page(page_number), 'tab_name': tag, 'name': tag, 'tag': tag, 'pagenation_link': pagenation_link})


def tags(request):
    items = Tag.objects.all()
    return render(request, 'tags_categories.html', {'param': items, 'name': 'Tags', 'url': 'tag'})


def page_not_found(request, exception=None):
     return render(request,'404.html')