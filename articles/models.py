from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from ckeditor.fields import RichTextField

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

class Category(models.Model):
    content = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.content
    

class Tag(models.Model):
    content = models.CharField(max_length=100)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.content


class Article(models.Model):
    status = models.IntegerField(choices=STATUS, default=0)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=350)
    author = models.ForeignKey(User, on_delete= models.CASCADE)

    #SEO
    keywords = models.CharField(max_length = 160, help_text="seperate keywords with comma")
    social_media_url = models.URLField(max_length = 300, blank=True)
    social_media_site_name = models.URLField(max_length = 300, blank=True)
    social_media_type = models.CharField(max_length = 200, help_text="What type is like website, article, blog", default="Blog")
    social_media_image = models.URLField(max_length = 300, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    created_date = models.DateField(auto_now_add = True)
    content = RichTextField(blank=True, null = True)
    updated_on = models.DateField(auto_now= True)
    image = models.ImageField(upload_to='articles/uploads/', blank=True)

    def __str__(self):
        return self.title + ' | ' + str(STATUS[self.status][1])
    