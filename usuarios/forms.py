from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UsuarioPersonalizado

class UsuarioPersonalizadoCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        fields = UserCreationForm.Meta.fields + ('idade',)

class UsuarioPersonalizadoChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = UsuarioPersonalizado
        fields = UserChangeForm.Meta.fields
        

