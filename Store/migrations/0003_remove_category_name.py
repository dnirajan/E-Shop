# Generated by Django 3.1.7 on 2022-03-05 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0002_auto_20220305_0924'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name',
        ),
    ]