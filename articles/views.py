from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Article


def index(request):
    return render(request, 'index.html')

def blog(request):
    articles = Article.objects.order_by('created_date')[:5]
    context = {'articles': articles}
    return render(request, 'blog.html', context)