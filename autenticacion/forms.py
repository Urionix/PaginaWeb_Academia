from django import forms
from django.contrib.auth.forms import UserCreationForm # importamos esta libreria, porque es donde se encuentra lo necesario para Registrar usuarios
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from autenticacion.models import User

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','DPI','fecha_nacimiento','Ubicacion']
        widgets={
            'fecha_nacimiento': forms.DateInput(attrs={'type':'date'}),
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

