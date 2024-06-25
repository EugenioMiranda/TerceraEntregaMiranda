from django.urls import path
from django.contrib.auth.views import LogoutView
from AppMiranda.views import *

urlpatterns = [
    path('agrega-producto/<nombre>/<marca>/<codigo>', producto),
    path('', inicio, name='Inicio'),
    path('productos/', productos, name='Productos'),
    path('clientes/', clientes, name='Clientes'),
    path('empleados/', empleados, name='Empleados'),
    path('producto-formulario/', producto_formulario, name='ProductoFormulario'),
    path('cliente-formulario/', cliente_formulario, name='ClienteFormulario'),
    path('empleado-formulario/', empleado_formulario, name='EmpleadoFormulario'),
    path('busqueda-codigo/', busqueda_codigo, name='BusquedaCodigo'),
    path('buscar/', buscar, name='BuscarCodigo'),
    path('lista-clientes/', lista_clientes, name='ListaClientes'),
    path('lista-empleados/', lista_empleados, name='ListaEmpleados'),
    path('lista-productos/', lista_productos, name='ListaProductos'),
    path('elimina-empleado/<int:id>', eliminar_empleado, name='EliminaEmpleado'),
    path('edita-empleado/<int:id>', editar_empleado, name='EditaEmpleado'),
    path('lista-producto/', ProductoList.as_view(), name='ListaProductos'),
    path('detalle-producto/<pk>', ProductoDetail.as_view(), name='DetalleProducto'),
    path('crea-producto/', ProductoCreate.as_view(), name='CreaProducto'),
    path('actualiza-producto/<pk>', ProductoUpdate.as_view(), name='ActualizaProducto'),
    path('elimina-producto/<pk>', ProductoDelete.as_view(), name='EliminaProducto'),
    path('login/', login_view, name='Login'),
    path('registrar/', register, name='Registrar'),
    path('logout/', LogoutView.as_view(template_name="logout.html"), name='Logout'),
]



