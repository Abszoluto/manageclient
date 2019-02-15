# Generated by Django 2.1.5 on 2019-02-11 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, null=True, verbose_name='E-MAIL')),
                ('datanasc', models.DateField()),
                ('endereco', models.CharField(max_length=300)),
                ('cpf', models.CharField(max_length=14, verbose_name='CPF')),
                ('rg', models.CharField(max_length=20)),
                ('cep', models.CharField(max_length=8)),
                ('telefone', models.CharField(max_length=11)),
            ],
        ),
    ]