# Generated by Django 4.2.7 on 2023-11-30 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('cargo', models.CharField(max_length=50)),
                ('cnh', models.CharField(max_length=20)),
                ('telefone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
