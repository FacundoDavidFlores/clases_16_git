from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Familiar    #Esto es un importe mio nuevo
from AppCoder.forms import Buscar, FamiliarForm
from django.views import View
# Create your views here.
def saludo(request):    #Consulta o peticion
    return HttpResponse("Hola mi primera app")
def saludo_dos(request):
    return HttpResponse("Este es otro saludo")
def saludo_a(request, nombre):
    return HttpResponse(f"Hola como estas {nombre}")
def mostrar_mi_template(request):
    return render(request, "AppCoder/index.html")
#---------------------------------------------------------------------------
def mostrar_familiares(request):
    lista_familiares = Familiar.objects.all()
    return render(request, "AppCoder/familiares.html", {"lista_familiares": lista_familiares})
#---------------------------------------------------------------------------
class BuscarFamiliar(View):
    form_class = Buscar
    template_name = 'AppCoder/buscar.html'
    initial = {"nombre": ""}
    #---------------------------------------------------------------------------
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})
    #---------------------------------------------------------------------------
    def post(self, request):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            nombre = form.cleaned_data.get("nombre")
            lista_familiares = Familiar.objects.filter(nombre__icontains=nombre).all()
            form = self.form_class(initial=self.initial)
            return render(request, self.template_name, {'form':form, 'lista_familiares':lista_familiares})
        return render(request, self.template_name, {"form": form})
    #---------------------------------------------------------------------------
#---------------------------------------------------------------------------
class AltaFamiliar(View):
    form_class = FamiliarForm
    template_name = 'AppCoder/alta_familiar.html'
    initial = {"nombre": "", "direccion": "", "numero_pasaporte": ""}
     #---------------------------------------------------------------------------
    def get(self, request):
        form = self.form_class(initial = self.initial)
        return render(request, self.template_name, {'form': form})
    #---------------------------------------------------------------------------
    def post(self, request):
        form = self.form_class(request.POST)
        if(form.is_valid()):
            form.save()
            msg_exito = f"se cargo con éxito el familiar {form.cleaned_data.get('nombre')}"
            form = self.form_class(initial = self.initial)
            return render(request, self.template_name, {'form':form, 'msg_exito':msg_exito})
        return render(request, self.template_name, {"form":form})
    #---------------------------------------------------------------------------
#---------------------------------------------------------------------------
