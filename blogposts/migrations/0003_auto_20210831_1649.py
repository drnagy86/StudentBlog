# Generated by Django 3.1.13 on 2021-08-31 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogposts', '0002_auto_20210831_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='blogpost',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogposts.blogpost'),
        ),
    ]
