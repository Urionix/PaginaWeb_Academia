# Generated by Django 4.2.5 on 2023-10-28 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacion', '0017_rename_bio_user_biografia_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Biografia',
            field=models.TextField(blank=True, max_length=100, null=True),
        ),
    ]
