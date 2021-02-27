from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Article


def index(request):
    return render(request, 'index.html')

def blog(request):
    articles = Article.objects.order_by('created_date')[:5]
    context = {'articles': articles}
    return render(request, 'blog.html', context)

def article(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    return render(request, 'article.html', {'article': article})