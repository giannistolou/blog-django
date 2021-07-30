from django.urls import path

from . import views, models

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<int:page_number>/', views.blog, name='blog'),
    path('article/<int:article_id>/', views.article, name='article'),
    path('tag/<int:tag_id>/', views.tag, name='tag'),
    path('category/<int:category_id>/', views.category, name='category'),
    path('tags', views.tags, name='tags'),
    path('categories', views.categories, name='categories'),
]