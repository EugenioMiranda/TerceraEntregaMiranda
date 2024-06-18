from django.urls import path
from AppMiranda.views import producto, lista_productos, inicio, productos, clientes, empleados, producto_formulario, busqueda_codigo, buscar

urlpatterns = [
    path('agrega-producto/<nombre>/<marca>/<codigo>', producto),
    path('lista-productos/', lista_productos),
    path('', inicio, name='Inicio'),
    path('productos/', productos, name='Productos'),
    path('clientes/', clientes, name='Clientes'),
    path('empleados/', empleados, name='Empleados'),
    path('producto-formulario/', producto_formulario, name='ProductoFormulario'),
    path('busqueda-codigo/', busqueda_codigo, name='BusquedaCodigo'),
    path('buscar/', buscar, name='BuscarCodigo'),
]


