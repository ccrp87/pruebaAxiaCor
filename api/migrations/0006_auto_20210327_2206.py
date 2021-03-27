# Generated by Django 3.1.3 on 2021-03-27 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210327_2151'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tarjeta',
            name='token',
        ),
        migrations.AddField(
            model_name='tarjeta',
            name='usuarioid',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.RESTRICT, to='api.usuario'),
        ),
    ]
