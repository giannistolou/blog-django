from django.db import models

# Create your models here.
class Article(models.Model, ):
    title = models.TextField(max_length=200)
    publication_date = models.DateTimeField('date published')
    text = models.TextField()
    image = models.ImageField(upload_to='uploads/% Y/% m/% d/')
