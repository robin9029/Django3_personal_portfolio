from django.shortcuts import render
from .models import Project          #import models i.e Table Project

# Create your views here.

def home(request):
    projects = Project.objects.all()  #taking  data from database
    return render(request,'portfolio/home.html',{'projects':projects})
