from django import forms

class PerfumeriaFormulario(forms.Form):
    nombre = forms.CharField()
    longitud = forms.FloatField()
    ancho = forms.FloatField()
    altura = forms.FloatField()
    peso = forms.FloatField()