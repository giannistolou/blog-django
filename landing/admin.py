from django.contrib import admin
from .models import Journey, Skill, Project, Information, Landing_seo
# Register your models here.
admin.site.register(Skill)
admin.site.register(Project)
admin.site.register(Information)
admin.site.register(Landing_seo)
admin.site.register(Journey)