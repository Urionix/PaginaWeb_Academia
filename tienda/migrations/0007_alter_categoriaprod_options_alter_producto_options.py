# Generated by Django 4.2.5 on 2023-10-24 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0006_alter_categoriaprod_options_alter_producto_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoriaprod',
            options={'verbose_name': 'CategoriaCursos', 'verbose_name_plural': 'CategoriasCursos'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'verbose_name': 'Curso', 'verbose_name_plural': 'Cursos'},
        ),
    ]
