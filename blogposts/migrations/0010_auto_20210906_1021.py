# Generated by Django 3.1.13 on 2021-09-06 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0009_auto_20210906_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='Anonymous', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='No comment', max_length=140, null=True),
        ),
    ]