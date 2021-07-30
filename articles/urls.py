from django.urls import path

from . import views, models

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:page_number>/', views.blog, name='blog'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('tag/<int:tag_id>/', views.tag, name='tag'),
    path('tag/<int:tag_id>/<int:page_number>/', views.tag, name='tag'),
    path('tags', views.tags, name='tags'),
]