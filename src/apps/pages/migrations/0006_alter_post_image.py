# Generated by Django 3.2.8 on 2022-02-21 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='static'),
        ),
    ]
