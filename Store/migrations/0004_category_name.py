# Generated by Django 3.1.7 on 2022-03-05 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0003_remove_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name',
            field=models.CharField(default='', max_length=50),
        ),
    ]
