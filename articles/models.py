from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="The url of the article. Must be unique!", default=datetime.now().strftime("%d-%m-%y") + '/')
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_article')
    created_date = models.DateTimeField('date published')
    content = models.TextField()
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to='uploads/% d/% m/% y/')
    