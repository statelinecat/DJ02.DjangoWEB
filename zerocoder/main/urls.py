
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('newnewnew', views.new, name='page2'),
    path('page3', views.new, name='page3'),
    path('page4', views.new, name='page4'),
]
