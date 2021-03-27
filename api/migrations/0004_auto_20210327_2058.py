# Generated by Django 3.1.3 on 2021-03-27 20:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='email',
            new_name='correo',
        ),
        migrations.AddField(
            model_name='usuario',
            name='fecha_creacion',
            field=models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Fecha Creación'),
        ),
        migrations.AlterField(
            model_name='tarjeta',
            name='uuid',
            field=models.UUIDField(auto_created=True, default=uuid.uuid4, verbose_name='UUID'),
        ),
    ]
