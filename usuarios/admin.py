from django.contrib import admin

# Register your models here.

from django.contrib.auth.admin import UserAdmin
from .forms import UsuarioPersonalizadoCreationForm
from .forms import UsuarioPersonalizadoChangeForm
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoAdmin(UserAdmin):
    add_form = UsuarioPersonalizadoCreationForm
    form = UsuarioPersonalizadoChangeForm
    model = UsuarioPersonalizado
    list_display = ['email','username','idade','is_staff',]


admin.site.register(UsuarioPersonalizado, UsuarioPersonalizadoAdmin)