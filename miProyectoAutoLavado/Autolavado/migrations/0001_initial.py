# Generated by Django 3.1.2 on 2020-10-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='auto',
            fields=[
                ('Seccion', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('Descripcion', models.CharField(max_length=100)),
            ],
        ),
    ]
