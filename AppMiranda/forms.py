from django import forms

class ProductoFormulario(forms.Form):
    producto = forms.CharField()
    marca = forms.CharField()
    codigo = forms.IntegerField()
