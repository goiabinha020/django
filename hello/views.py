from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    #renderizar arquivos html
    return render(request, "hello/index.html")

def eu(request):
    return HttpResponse("Hello, guilherme")

def lucas(request):
    return HttpResponse("Hello, Lucas")

def greet(request, name):
   return render(request, "hello/greet.html", {"name" : name.capitalize()})