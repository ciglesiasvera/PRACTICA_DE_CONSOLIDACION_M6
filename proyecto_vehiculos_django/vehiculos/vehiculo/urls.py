from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.add_vehiculo, name='add_vehiculo'),
    path('vehiculo/list/', views.list_vehiculos, name='list_vehiculos'),
]