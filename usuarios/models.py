from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizado(AbstractUser):
    idade = models.PositiveIntegerField(null=True, blank=True)
