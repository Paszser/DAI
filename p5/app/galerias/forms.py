from django import forms
from .models import Galeria, Cuadro
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioGaleria(forms.ModelForm):
    class Meta:
        model = Galeria
        fields = '__all__'
        widgets = {}

class FormularioCuadro(forms.ModelForm):
    class Meta:
        model = Cuadro
        fields = '__all__'
        widgets = {}

class FormularioRegistro(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']