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