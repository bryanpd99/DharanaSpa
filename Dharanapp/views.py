from django.shortcuts import render
from django.http import HttpResponse
from DharanAPI.models import *
# action que devuelve la vista de la pagina de inicio
def vindex(request):
    return render(request,'index.html')
# action que devuelve la vista de la pagina de inicio
def vreserva(request):
    return render(request,'reserva.html')
def vservicio(request):
    Trat=Tratamiento.objects.all()
    ctx={'tratamientos':Trat}
    return render(request,'servicios.html',ctx)
def vgestion(request):
    return render(request,'gestion.html')




# Create your views here.
