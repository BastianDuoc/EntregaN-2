# Generated by Django 3.1.2 on 2020-10-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Autolavado', '0003_auto_20201018_0828'),
    ]

    operations = [
        migrations.CreateModel(
            name='MisionVision',
            fields=[
                ('ident', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('mision', models.TextField(max_length=255)),
                ('vision', models.TextField(max_length=255)),
            ],
        ),
    ]
