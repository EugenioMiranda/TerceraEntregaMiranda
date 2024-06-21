from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Cliente, Empleado
from .forms import ProductoFormulario, ClienteFormulario, EmpleadoFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Create your views here.
def producto(req, nombre, marca, codigo):
    nuevo_producto = Producto(nombre=nombre, marca=marca, codigo=codigo)
    nuevo_producto.save()

    return HttpResponse(f"""
        <p>Producto: {nuevo_producto.nombre} - Marca: {nuevo_producto.marca} - Codigo: {nuevo_producto.codigo} Creado! </p>
    """)



def inicio(req):
    return render (req, "inicio.html", {})

def productos(req):
    return render (req, "productos.html", {})

def clientes(req):
    return render (req, "clientes.html", {})

def empleados(req):
    return render (req, "empleados.html", {})







def producto_formulario(req):

    if req.method == 'POST':

        miFormulario = ProductoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            nuevo_producto = Producto(nombre=data['nombre'], marca=data['marca'], codigo=data['codigo'])
            nuevo_producto.save()
            return render (req, "inicio.html", {"mesage": "Curso creado con exito"})
        
        else:
            return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:
        miFormulario = ProductoFormulario()
        return render (req, "producto_formulario.html", {"miFormulario": miFormulario})
    

    




def busqueda_codigo(req):
    return render (req, "busqueda_codigo.html", {})


def buscar(req):
     
     if req.GET["codigo"]:
         codigo=req.GET["codigo"]
         nombre=Producto.objects.get(codigo=codigo)
         return render (req, "resultadoBusqueda.html", {"nombre": nombre, "codigo": codigo})
     
     else:
         return render (req, "inicio.html", {"mesage": "No enviaste el dato del codigo"})
     










def cliente(req, nombre, apellido, dni, email):
    nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, dni=dni, email=email)
    nuevo_cliente.save()

    return HttpResponse(f"""
        <p>Nombre: {nuevo_cliente.nombre} - Apellido: {nuevo_cliente.marca} - Email: {nuevo_cliente.email} - DNI: {nuevo_cliente.dni} Creado! </p>
    """)




def cliente_formulario(req):

    if req.method == 'POST':

        miFormulario = ClienteFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            nuevo_producto = Cliente(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], dni=data['dni'])
            nuevo_producto.save()
            return render (req, "inicio.html", {"mesage": "Registrado con exito"})
        
        else:
            return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:
        miFormulario = ClienteFormulario()
        return render (req, "cliente_formulario.html", {"miFormulario": miFormulario})
    









def cliente(req, nombre, apellido, dni, email):
    nuevo_cliente = Cliente(nombre=nombre, apellido=apellido, dni=dni, email=email)
    nuevo_cliente.save()

    return HttpResponse(f"""
        <p>Nombre: {nuevo_cliente.nombre} - Apellido: {nuevo_cliente.marca} - Email: {nuevo_cliente.email} - DNI: {nuevo_cliente.dni} Creado! </p>
    """)




def empleado_formulario(req):

    if req.method == 'POST':

        miFormulario = EmpleadoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            nuevo_empleado = Empleado(nombre=data['nombre'], apellido=data['apellido'], email=data['email'], dni=data['dni'])
            nuevo_empleado.save()
            return render (req, "inicio.html", {"mesage": "Registrado con exito"})
        
        else:
            return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:
        miFormulario = EmpleadoFormulario()
        return render (req, "empleado_formulario.html", {"miFormulario": miFormulario})
    

    


def lista_clientes(req):

    mis_clientes = Cliente.objects.all()

    return render (req, "leer_clientes.html", {"clientes": mis_clientes})



def lista_empleados(req):

    mis_empleados = Cliente.objects.all()

    return render (req, "leer_empleados.html", {"empleados": mis_empleados})


def lista_productos(req):

    mis_productos = Producto.objects.all()

    return render (req, "leer_productos.html", {"productos": mis_productos})



def eliminar_empleado(req, id):

    if req.method == 'POST':

        empleado = Empleado.objects.get(id=id)
        empleado.delete()

        mis_empleados = Empleado.objects.all()
    return render (req, "leer_empleados.html", {"empleados": mis_empleados})



def editar_empleado(req, id):

    if req.method == 'POST':

        miFormulario = EmpleadoFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            empleado = Empleado.objects.get(id=id)
            empleado.nombre = data ["nombre"]
            empleado.apellido = data ["apellido"]
            empleado.email = data ["email"]
            empleado.dni = data ["dni"]

            empleado.save()
         
            return render (req, "inicio.html", {"mesage": "Actualizado con exito"})
        
        else:
            return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:

        empleado = Empleado.objects.get(id=id)

        miFormulario = EmpleadoFormulario(initial={
            "nombre": empleado.nombre,
            "apellido": empleado.apellido,
            "email": empleado.email,
            "dni": empleado.dni,
        })
        return render (req, "editar_empleado.html", {"miFormulario": miFormulario, "id": empleado.id})
    

class ProductoList(ListView):

    model = Producto