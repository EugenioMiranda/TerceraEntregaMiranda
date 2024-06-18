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

        nuevo_producto = Producto(nombre=req.POST['nombre'], marca=req.POST['marca'], codigo=req.POST['codigo'])
        nuevo_producto.save()
        return render (req, "inicio.html", {})

    else:
        miFormulario = ProductoFormulario()
        return render (req, "producto_formulario.html", {"miFormulario": miFormulario})