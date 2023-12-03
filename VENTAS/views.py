from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from VENTAS.models import medicamentos, perfumeria, suplementos
from VENTAS.forms import PerfumeriaFormulario

# Create your views here.

def principal(request):
    return render(request, "index.html")

def carga_medicamento(request):
    
    if request.method == "POST":
        nuevo_medicamento = medicamentos(
            nombre = request.POST["nombre"],
            longitud = request.POST["longitud"],
            ancho = request.POST["ancho"],
            altura = request.POST["altura"],
            peso = request.POST["peso"]
        )
        nuevo_medicamento.save()
        return render(request, "mensaje.html")
    return render(request, "medicamento_formulario.html")

#Como en clase no pude ver cómo colocar el botón "Enviar", decidí no usar este método, ya que apretando enter igual no podia mandar el formulario

#def carga_perfumeria(request):
#    
#    if request.method == "POST":
#        nuevo_formulario = PerfumeriaFormulario(request.POST)
#        if nuevo_formulario.is_valid:
#            informacion = nuevo_formulario.cleaned_data
#            perfume = perfumeria(
#                nombre = informacion["nombre"],
#                longitud = informacion["longitud"],
#                ancho = informacion["ancho"],
#                altura = informacion["altura"],
#                peso = informacion["peso"],
#            )
#            perfume.save()
#            return render(request, "mensaje.html") 
#    else:
#        nuevo_formulario = PerfumeriaFormulario()
#        return render(request, "perfumeria_formulario.html", {"formulario": nuevo_formulario})

def carga_perfumeria(request):
    
    if request.method == "POST":
        nuevo_perfume = perfumeria(
            nombre = request.POST["nombre"],
            longitud = request.POST["longitud"],
            ancho = request.POST["ancho"],
            altura = request.POST["altura"],
            peso = request.POST["peso"]
        )
        nuevo_perfume.save()
        return render(request, "mensaje.html")
    return render(request, "perfumeria_formulario2.html")

def carga_suplemento(request):
    if request.method == "POST":
        nuevo_suplemento = suplementos(
        nombre = request.POST["nombre"],
        longitud = request.POST["longitud"],
        ancho = request.POST["ancho"],
        altura = request.POST["altura"],
        peso = request.POST["peso"]
        )
        nuevo_suplemento.save()
        return render(request, "mensaje.html")
    return render(request, "suplemento_formulario.html")

