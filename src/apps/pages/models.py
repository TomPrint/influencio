from django.db import models
from django.urls import reverse
from django.utils import timezone

class Movie (models.Model):
    author = models.CharField(max_length=50, verbose_name='Nazwa influencera')
    title = models.CharField(max_length=50, verbose_name='Nazwa filmu')
    category = models.CharField(max_length=50, verbose_name='Kategoria filmu')
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

# Create your models here.
