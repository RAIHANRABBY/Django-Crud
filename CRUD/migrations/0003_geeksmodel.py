# Generated by Django 4.1.4 on 2022-12-27 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRUD', '0002_remove_product_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeeksModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
            ],
        ),
    ]
