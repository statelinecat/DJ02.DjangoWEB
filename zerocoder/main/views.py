from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Это мой первый проект Django!</h1>") #render(request, 'main/index.html')

def new(request):
    return HttpResponse("<h1>Это вторая страница моего проекта Django!</h1>")