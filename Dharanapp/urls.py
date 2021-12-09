from django.conf import urls
from django.urls import path
from . import views
urlpatterns=[
    path('',views.vindex, name='pinicio'),
    path('inicio/',views.vindex, name='pinicio'),
    path('reserva/',views.vreserva, name='preserva'),
    path('servicio/',views.vservicio, name='pservicio'),
    #path('gestion/',views.vgestion, name='pgestion')
]