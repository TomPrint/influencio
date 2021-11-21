from django.db import models
from django.urls import reverse
from django.utils import timezone


category_choices = (
    ('HOT-TOP', 'HOT-TOP'), ('ODKRYCIA', 'ODKRYCIA'), ('BEAUTY','BEAUTY'), ('ŚMIESZNE', 'ŚMIESZNE'),
    ('GAMING', 'GAMING'), ('LIFESTYLE', 'LIFESTYLE'), ('SZTUKA', 'SZTUKA'), ('SPORT','SPORT'),)

source_choices = (
    ('YouTube', 'YouTube'), ('TikTok', 'TikTok'), ('Instagram','Instagram'), ('Other', 'Other'), ('Promo', 'Promo'),)
# Create your models here.

class Movie (models.Model):
    category = models.CharField(max_length=50, verbose_name='Kategoria filmu', default= 'unassigned', null=False, choices=category_choices)
    source = models.CharField(max_length=50, verbose_name='Źródło filmu', default= 'unassigned', null=False, choices=source_choices)
    promotion = models.BooleanField(default=False, verbose_name='PROMOCJA FILMU')
    author = models.CharField(max_length=50, verbose_name='Nazwa influencera')
    title = models.CharField(max_length=50, verbose_name='Nazwa filmu')
    content = models.TextField(max_length=10000, verbose_name='HTML EMBEDED do filmu')
    date_posted = models.DateTimeField(default=timezone.now)
    youtube_url = models.URLField(blank=True, max_length=300)
    tiktok_url = models.URLField(blank=True, max_length=300)
    insta_url = models.URLField(blank=True, max_length=300)
    

    class Meta:
        verbose_name = ("Movie")
        verbose_name_plural = ("Movies")

    def __str__(self):
        return self.author +' - '+ self.title 

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})



