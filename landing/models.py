from django.db import models

KNOWLEDGE = (
    (2,"Very Good"),
    (1,"Good"),
    (0,"Familiar"),
)

THEME = (
    ("primary", "primary"),
    ("link", "link"),
    ("info", "info"),
    ("success", "success"),
    ("warning", "warning"),
    ("danger", "danger"),
    ("dark","dark"),
    ("light","light")
)

class Skill(models.Model):
    name= models.CharField(max_length = 100)
    knowledge = models.IntegerField(choices=KNOWLEDGE, default=0)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length = 100)
    context = models.TextField(max_length = 500)
    project_link = models.URLField(max_length = 300, blank = True)
    article_link = models.URLField(max_length = 300, blank = True)

    def __str__(self):
        return self.name

class Journey(models.Model):
    title = models.CharField(max_length = 100)
    organization = models.CharField(max_length = 100, blank= True)
    description = models.TextField(max_length = 500, blank= True)
    from_date = models.DateField()
    to_date = models.DateField()
    until_present_to_date = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Information(models.Model):
    name = models.CharField(max_length = 100)
    subtitle_name = models.CharField(max_length = 200, default="")
    summary = models.TextField(max_length = 300, default="")
    gitlab_link = models.URLField(max_length = 300, blank = True)
    github_link = models.URLField(max_length = 300, blank = True)
    linkedin_link = models.URLField(max_length = 300, blank = True)
    facebook_link = models.URLField(max_length = 300, blank = True)
    instagram_link = models.URLField(max_length = 300, blank = True)
    twitter_link = models.URLField(max_length = 300, blank = True)
    youtube_link = models.URLField(max_length = 300, blank = True)
    theme = models.TextField(choices=THEME, default='info')

    def __str__(self):
        return self.name

class Landing_seo(models.Model):
    description = models.CharField(max_length = 150)
    keywords = models.CharField(max_length = 160, help_text="seperate keywords with comma")
    author = models.CharField(max_length = 100)
    social_media_url = models.URLField(max_length = 300, blank=True)
    social_media_site_name = models.URLField(max_length = 300, blank=True)
    social_media_type = models.CharField(max_length = 200)
    social_media_image = models.URLField(max_length = 300, blank=True)
    

