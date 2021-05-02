from django.db import models

KNOWLEDGE = (
    (2,"Very Good"),
    (1,"Good"),
    (0,"Familiar"),
)

class Skill(models.Model):
    name= models.CharField(max_length = 100)
    knowledge = models.IntegerField(choices=KNOWLEDGE, default=0)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length = 100)
    context = models.TextField(max_length = 300)
    project_link = models.URLField(max_length = 300, blank = True)
    article_link = models.URLField(max_length = 300, blank = True)

    def __str__(self):
        return self.name

class Information(models.Model):
    name = models.CharField(max_length = 100)
    subtitle_name = models.CharField(max_length = 200, default="")
    summary = models.TextField(max_length = 300, default="")
    gitlab_link = models.URLField(max_length = 300, blank = True)
    github_link = models.URLField(max_length = 300, blank = True)
    linkedin_link = models.URLField(max_length = 300, blank = True)

    def __str__(self):
        return self.name


