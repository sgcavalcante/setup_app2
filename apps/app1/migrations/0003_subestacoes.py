# Generated by Django 4.2.5 on 2023-09-19 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_contatos1'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subestacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subestacao', models.CharField(max_length=20)),
                ('nivel_de_tensao', models.CharField(max_length=6)),
                ('descricao', models.TextField(max_length=100)),
            ],
        ),
    ]
