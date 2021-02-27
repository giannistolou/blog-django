from django.urls import path

from . import views, models

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('tag/<int:tag_id>/', views.tag, name='tag')
]