from django import forms

class ProductoFormulario(forms.Form):
    nombre = forms.CharField()
    marca = forms.CharField()
    codigo = forms.IntegerField()


class ClienteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    dni = forms.IntegerField()


