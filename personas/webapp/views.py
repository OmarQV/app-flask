from django.shortcuts import render

# Importams HTTP
from django.http import HttpResponse

# Create your views here.
def bienvenido(request):
   return HttpResponse('Hola mundo desde DJANGO')

def despedida(request):
   return HttpResponse('Despedida')