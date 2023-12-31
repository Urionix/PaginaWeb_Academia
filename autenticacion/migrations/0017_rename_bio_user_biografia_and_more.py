# Generated by Django 4.2.5 on 2023-10-28 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0016_rename_perfil_user_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='bio',
            new_name='Biografia',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='picture',
            new_name='Foto_perfil',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='location',
            new_name='Ubicacion',
        ),
        migrations.AddField(
            model_name='user',
            name='DPI',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True),
        ),
    ]
