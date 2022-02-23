from django.contrib import sitemaps
from django.urls import reverse


class StaticViewsSitemap(sitemaps.Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    # The below method returns all urls defined in urls.py file

    def items(self):

        return [
            'page-home', 
            'page-travel', 
            'page-sztuka', 
            'page-beauty', 
            'page-funny', 
            'page-lifestyle', 
            'page-gaming', 
            'page-sport', 
            'page-contact', 
            'page-privacy',
            'page-about',
            'page-about',
            'page-creators',
            'page-articles',
            ]

    def location(self, item):
        return reverse(item)