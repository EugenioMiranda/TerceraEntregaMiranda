from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto, Cliente, Empleado, Avatar
from .forms import ProductoFormulario, ClienteFormulario, EmpleadoFormulario, AvatarFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def producto(req, nombre, marca, codigo):
    nuevo_producto = Producto(nombre=nombre, marca=marca, codigo=codigo)
    nuevo_producto.save()

    return HttpResponse(f"""
        <p>Producto: {nuevo_producto.nombre} - Marca: {nuevo_producto.marca} - Codigo: {nuevo_producto.codigo} Creado! </p>
    """)



def inicio(req):

    try:
        avatar = Avatar.objects.get(user = req.user.id)
        return render (req, "inicio.html", {"url":avatar.imagen.url})
        
    except:
        return render (req, "inicio.html")


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
        empleado = get_object_or_404(Empleado, id=id)
        empleado.delete()
        mis_empleados = Empleado.objects.all()
        return render(req, "leer_empleados.html", {"empleados": mis_empleados})

    
    return redirect('ListaEmpleados')



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
    template_name = 'producto_list.html'
    context_object_name = "productos"


class ProductoDetail(DeleteView):

    model = Producto
    template_name = 'producto_detail.html'
    context_object_name = "producto"

class ProductoCreate(CreateView):

    model = Producto
    template_name = 'producto_create.html'
    fields = ["nombre", "camada"]
    success_url = "/app-miranda/"

class ProductoUpdate(UpdateView):

    model = Producto
    template_name = 'producto_update.html'
    fields = ('__all__')
    success_url = "/app-miranda/"
    context_object_name = "producto"

class ProductoDelete(DeleteView):

    model = Producto
    template_name = 'producto_delete.html'
    success_url = "/app-miranda/"



def login_view(req):
    if req.method == 'POST':

            miFormulario = AuthenticationForm(req, data=req.POST)

            if miFormulario.is_valid():

                data = miFormulario.cleaned_data

                usuario=data["username"]
                psw=data["password"]
                user = authenticate(username=usuario, password=psw)

                if user:
                    login(req, user)
                    return render (req, "inicio.html", {"mesage": f"Bienvenido {usuario}"})

                else:

                    return render (req, "inicio.html", {"mesage": "Datos erroneos"})
            
            else:
                return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:
        miFormulario = AuthenticationForm()
        return render (req, "login.html", {"miFormulario": miFormulario})
    



def register(req):

    if req.method == 'POST':

            miFormulario = UserCreationForm(req.POST)

            if miFormulario.is_valid():

                data = miFormulario.cleaned_data

                usuario=data["username"]
                miFormulario.save()

                return render (req, "inicio.html", {"mesage": f"Usuario {usuario} creado con exito!"})
            
            else:
                return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:
        miFormulario = UserCreationForm()
        return render (req, "registro.html", {"miFormulario": miFormulario})

        
@login_required()        
def editar_perfil(req):

    usuario = req.user

    if req.method == 'POST':

        miFormulario = UserChangeForm(req.POST, instance=req.user)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            usuario.first_name = data ["first_name"]
            usuario.last_name = data ["last_name"]
            usuario.email = data ["email"]
            usuario.set_password(data["password1"])
            

            usuario.save()
         
            return render (req, "inicio.html", {"mesage": "Actualizado con exito"})
        
        else:
            return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:


        miFormulario = UserChangeForm(instance=req.user)
        return render (req, "editar_perfil.html", {"miFormulario": miFormulario})
    

def agregar_avatar(req):

    if req.method == 'POST':

        miFormulario = AvatarFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            avatar = Avatar(user=req.user, imagen=data("magen"))
            avatar.save()
         
            return render (req, "inicio.html", {"mesage": "Avatar cargado con exito"})
        
        else:
            return render (req, "inicio.html", {"mesage": "Datos invalidos"})

    else:

        miFormulario = AvatarFormulario()
        return render (req, "agregar_avatar.html", {"miFormulario": miFormulario})