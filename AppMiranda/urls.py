from django.urls import path
from AppMiranda.views import producto, lista_productos, inicio, productos, clientes, empleados, producto_formulario, busqueda_codigo, buscar, cliente_formulario, empleado_formulario, lista_clientes, lista_empleados, eliminar_empleado, editar_empleado

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
]



