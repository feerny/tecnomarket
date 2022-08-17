from django.urls import path

from .views import *

urlpatterns = [
    path('',home,name="home" ),
    path('contacto/',contacto,name="contacto" ),
    path('galeria/',galeria,name="galeria" ),
    path('agregar_producto/',agregar_producto,name="agregar_producto" ),
    path('listar_productos/',listar_productos,name="listar_productos" ),
    path('modificar_producto/<id>/',modificar_producto,name="modificar_producto" ),
    path('eliminar_producto/<id>/',eliminar_producto,name="eliminar_producto" ),
]
