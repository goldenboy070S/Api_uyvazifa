# Generated by Django 5.1.1 on 2024-09-22 07:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_new_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car',
            name='image',
        ),
        migrations.RemoveField(
            model_name='new',
            name='image',
        ),
        migrations.RemoveField(
            model_name='product',
            name='image',
        ),
    ]
