# Generated by Django 4.2.5 on 2023-10-28 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0020_alter_user_foto_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Foto_perfil',
            field=models.ImageField(default='profile_default.png', upload_to='users/'),
        ),
    ]
