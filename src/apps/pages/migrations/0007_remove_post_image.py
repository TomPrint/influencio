# Generated by Django 3.2.8 on 2022-02-21 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_post_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
    ]
