# Generated by Django 3.2 on 2021-06-22 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_moviedirector_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='moviedirector',
            name='post',
        ),
    ]
