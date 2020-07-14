from django.shortcuts import render
from django.views.generic import TemplateView   


def home(request):
    return render(request, "core/home.html")

def sample(request):
    return render(request, "core/sample.html")