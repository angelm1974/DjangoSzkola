from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj użytkowniku!!!")

# Create your views here.
