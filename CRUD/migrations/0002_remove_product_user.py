# Generated by Django 4.1.4 on 2022-12-27 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
