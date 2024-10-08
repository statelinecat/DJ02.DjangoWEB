from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    data = {
        'caption': "График",
        }
    return render(request, 'main/index.html', context=data) #, context:{'caption':"График"})

def new(request):
    return render(request, 'main/new.html', context={'caption':"График2"})

def page3(request):
    return render(request, 'main/page3.html', context={'caption':"График3"})

def page4(request):
    return render(request, 'main/page4.html', context={'caption':"График4"})