from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('author','title','category','source','promotion','date_posted')

# Register your models here.
admin.site.register(Movie, MovieAdmin)

