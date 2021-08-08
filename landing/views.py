from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Landing_seo, Skill, Project, Information


def index(request):
    skills = Skill.objects.order_by('-knowledge')
    projects = Project.objects.all()
    informations = Information.objects.all()[0]
    try:
        seo = Landing_seo.objects.all()[0]
    except:
        seo = []

    context = {'skills': skills, 'projects': projects, 'informations': informations, 'seo': seo}
    return render(request, 'index.html', context)