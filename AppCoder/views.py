from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def saludo(request):    #Consulta o peticion
    return HttpResponse("Hola mi primera app")
def saludo_dos(request):
    return HttpResponse("Este es otro saludo")
def saludo_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")
def mostrar_mi_template(request):
    return render(request, "AppCoder/index.html")
# Blablablablablabla