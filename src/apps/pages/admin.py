from django.contrib import admin
from django.http.response import HttpResponse
from django.urls import path
from django.shortcuts import render
from django import forms

from .models import Movie
import csv

class ImportCsvForm(forms.Form):
    list_display = forms.FileField()


class MovieAdmin(admin.ModelAdmin):
    list_display = ('author','title','category','source','promotion','date_posted')
    #admin filter
    list_filter = ('author', 'title', )
    #admin search
    search_fields = ['author', 'title',]

    #urls for CSV dupload & download
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload-csv/', self.upload_csv),
            path('download-csv/', self.download_csv),
            path('download-csv/export', self.export),
            ]
        return new_urls + urls

    #CSV Querry
    def export(request, self):
        response = HttpResponse(content_type='text/csv')
        writer = csv.writer(response)
        writer.writerow (['Category', 'Source ','Promotion', 'Author', 'Title', 'Content', 'Date Posted', 'Youtube URL', 'Tiktok URL', 'Insta URL'])

        for movie in Movie.objects.all().values_list('category', 'source','promotion', 'author', 'title', 'content', 'date_posted', 'youtube_url', 'tiktok_url', 'insta_url'):
            writer.writerow(movie)
        
        response['Content-Disposition'] = 'attachement; filename="movies.csv"'
      
        return response


    #views for CSV download page  
    def download_csv(self, request):
        return render(request, 'admin/csv_download.html')


    #views for CSV upload page
    def upload_csv(self, request):
        if request.method == 'POST':
            csv_file = request.FILES["csv_upload"]

            file_data = csv_file.read().decode('utf-8')
            csv_data = file_data.split("\n")
            
            for x in csv_data:
                fields = x.split(";")


        form = ImportCsvForm()
        data = {"form": form}
        return render(request, 'admin/csv_upload.html', data)





# Register your models here.
admin.site.register(Movie, MovieAdmin)

