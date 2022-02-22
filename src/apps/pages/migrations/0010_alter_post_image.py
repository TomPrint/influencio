# Generated by Django 3.2.8 on 2022-02-22 00:17

from django.db import migrations, models
import pathlib


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0009_alter_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=pathlib.PureWindowsPath('media/newfile')),
        ),
    ]
