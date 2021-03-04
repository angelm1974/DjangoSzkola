from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Witaj użytkowniku!!!")

def detail(request, pytanie_id):
    return HttpResponse(f"Dostaniesz odpowiedz na pytanie {pytanie_id}")

def wynik(request, pytanie_id):
    return HttpResponse(f"Dostaniesz wyniki do pytania {pytanie_id}")
 
def glosuj(request, pytanie_id):
    return HttpResponse(f"Głosujesz na pytanie {pytanie_id}")
# Create your views here.
