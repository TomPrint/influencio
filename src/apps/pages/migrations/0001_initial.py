# Generated by Django 3.2.8 on 2022-01-04 00:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IpModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=100, verbose_name='IP')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('HOT-TOP', 'HOT-TOP'), ('ODKRYCIA', 'ODKRYCIA'), ('BEAUTY', 'BEAUTY'), ('ŚMIESZNE', 'ŚMIESZNE'), ('GAMING', 'GAMING'), ('LIFESTYLE', 'LIFESTYLE'), ('SZTUKA', 'SZTUKA'), ('SPORT', 'SPORT')], default='unassigned', max_length=50, verbose_name='Kategoria filmu')),
                ('source', models.CharField(choices=[('YouTube', 'YouTube'), ('TikTok', 'TikTok'), ('Instagram', 'Instagram'), ('Other', 'Other')], default='unassigned', max_length=50, verbose_name='Źródło filmu')),
                ('promotion', models.BooleanField(default=False, verbose_name='PROMOCJA FILMU')),
                ('author', models.CharField(max_length=50, verbose_name='Nazwa influencera')),
                ('title', models.CharField(max_length=50, verbose_name='Nazwa filmu')),
                ('content', models.TextField(max_length=10000, verbose_name='HTML EMBEDED do filmu')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('youtube_url', models.URLField(blank=True, max_length=300)),
                ('tiktok_url', models.URLField(blank=True, max_length=300)),
                ('insta_url', models.URLField(blank=True, max_length=300)),
                ('fire_likes', models.ManyToManyField(blank=True, related_name='fire_likes', to='pages.IpModel')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
