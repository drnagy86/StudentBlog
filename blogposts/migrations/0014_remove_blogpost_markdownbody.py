# Generated by Django 3.1.13 on 2021-10-02 21:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0013_auto_20211002_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='markDownBody',
        ),
    ]