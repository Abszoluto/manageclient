# Generated by Django 2.1.5 on 2019-02-14 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0004_auto_20190211_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='clientes.Cliente'),
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='responsavel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsavel', to=settings.AUTH_USER_MODEL),
        ),
    ]
