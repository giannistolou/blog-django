from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Skill, Project


def index(request):
    skills = Skill.objects.order_by('-knowledge')
    projects = Project.objects.all()
    context = {'skills': skills, 'projects': projects}
    return render(request, 'index.html', context)