from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from tinymce.models import HTMLField

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    content = models.CharField(max_length=100)

class Tag(models.Model):
    content = models.CharField(max_length=100)


class Article(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, help_text="The url of the article. Must be unique!", default=datetime.now().strftime("%d-%m-%y") + '/')
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField('date published')
    content = HTMLField()
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to='uploads/% d/% m/% y/')
    