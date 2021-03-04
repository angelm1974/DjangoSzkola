from django.urls import path
from .import views
urlpatterns = [
    path('',views.index, name='index'),
    
    path('<int:pytanie_id>/',views.detail, name='detail'),
    
    path('<int:pytanie_id>/wynik/',views.wynik, name='wynik'),
    
    path('<int:pytanie_id>/glosuj/',views.glosuj, name='glosuj'),
]