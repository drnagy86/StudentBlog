# Generated by Django 3.1.13 on 2021-09-01 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0006_auto_20210901_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='author',
        ),
    ]
