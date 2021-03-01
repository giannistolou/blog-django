from django.db import models

KNOWLEDGE = (
    (2,"Very Good"),
    (1,"Good"),
    (0,"Familiar"),
)

class Skill(models.Model):
    name= models.CharField(max_length = 100)
    knowledge = models.IntegerField(choices=KNOWLEDGE, default=0)

class Project(models.Model):
    name = models.CharField(max_length = 100)
    context = models.TextField(max_length = 300)
    link = models.URLField(max_length = 300, blank = True)


