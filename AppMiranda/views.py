from django.http import HttpResponse
from django.shortcuts import render
from .models import Producto, Cliente, Empleado
from .forms import ProductoFormulario

# Create your views here.
def producto(req, nombre, marca, codigo):
    nuevo_producto = Producto(nombre=nombre, marca=marca, codigo=codigo)
    nuevo_producto.save()

    return HttpResponse(f"""
        <p>Producto: {nuevo_producto.nombre} - Marca: {nuevo_producto.marca} - Codigo: {nuevo_producto.codigo} Creado! </p>
    """)


def lista_productos(req):
    lista = Producto.objects.all()

    return render (req, "lista_productos.html", {"lista_productos": lista})

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
     