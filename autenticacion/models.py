from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    Foto_perfil=models.ImageField(default='profile_default.png',upload_to='users/',null=True)
    Ubicacion=models.CharField(max_length=60, null=True, blank=True)
    Biografia=models.TextField(max_length=100, null=True, blank=True)
    DPI=models.BigIntegerField(null=True, blank=True)
    fecha_nacimiento=models.DateField(null=True, blank=True)

