# Generated by Django 4.2.5 on 2023-10-25 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0014_rename_perfil_user_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='picture',
            new_name='perfil',
        ),
    ]
