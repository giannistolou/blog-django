from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField
from datetime import datetime

# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content
    

class Tag(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Article(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateTimeField('date published')
    content = RichTextField(blank=True, null = True)
    updated_on = models.DateTimeField(auto_now= True)
    image = models.ImageField(upload_to='articles/uploads/% d/% m/% y/')

    def __str__(self):
        return self.title
    