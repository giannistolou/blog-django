from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Skill, Project, Information


def index(request):
    skills = Skill.objects.order_by('-knowledge')
    projects = Project.objects.all()
    informations = Information.objects.all()[0]
    context = {'skills': skills, 'projects': projects, 'informations': informations}
    return render(request, 'index.html', context)