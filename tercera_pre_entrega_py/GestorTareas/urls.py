from django.urls import path
from GestorTareas import views

#Se definen las urls dentro de la app 'GestorTareas', se indica la url, la view y por ultimo un nombre 

urlpatterns = [
    path('',views.inicio,name="Inicio"),
    path('tareas/', views.tareas,name="Tareas"),
    path("usuarios/",views.usuarios,name="Usuarios"),
    path("about/",views.about,name="About"),
    path('busquedadetareas/',views.busquedatareas,name="BusquedaTareas"),
]
