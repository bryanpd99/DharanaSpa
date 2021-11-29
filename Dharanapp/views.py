from django.shortcuts import render
from django.http import HttpResponse
# action que devuelve la vista de la pagina de inicio
def vindex(request):
    return render(request,'index.html')
# action que devuelve la vista de la pagina de inicio
def vreserva(request):
    return render(request,'reserva.html')
def vservicio(request):
    return render(request,'servicios.html')
def vgestion(request):
    return render(request,'gestion.html')




# Create your views here.
