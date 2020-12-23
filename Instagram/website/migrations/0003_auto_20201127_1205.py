# Generated by Django 3.1.1 on 2020-11-27 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20201127_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', editable=False, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='slug',
            field=models.SlugField(default='', editable=False, null=True, unique=True),
        ),
    ]
