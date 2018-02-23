from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def login(request):
    return render(request,"login.html")

def search(request):
    return render(request,"search.html")


# Create your views here.
