from django.urls import path
from AppMiranda.views import producto, lista_productos, inicio, productos, clientes, empleados

urlpatterns = [
    path('agrega-producto/<nombre>/<marca>/<codigo>', producto),
    path('lista-productos/', lista_productos),
    path('', inicio),
    path('productos/', productos),
    path('clientes/', clientes),
    path('empleados/', empleados),
]
