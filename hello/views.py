from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def rochelka(request):
    return HttpResponse("Hello my lovely Rochelka!")

def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })