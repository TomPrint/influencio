from django.contrib import admin, messages
from django.contrib.admin.decorators import action
from django.forms import fields
from django.http.response import HttpResponse
from django.contrib import messages
from django.urls import path
from django.shortcuts import render
from django.shortcuts import redirect
from django import forms
from django.utils.translation import ngettext

from .models import Movie
from .models import IpModel
import csv

from .models import Post


class ImportCsvForm(forms.Form):
    csv_upload = forms.FileField()


class MovieAdmin(admin.ModelAdmin):
    list_display = ('author','title','category','source','promotion','date_posted', 'fire_likes_count',)
    #admin filter
    list_filter = ('author', 'title', )
    #admin search
    search_fields = ['author', 'title',]
    #action 
    actions=['make_promotion', 'cancel_promotion',]



    #urls for CSV upload & download
    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload-csv/', self.upload_csv),
            path('download-csv/', self.download_csv),
            path('download-csv/export', self.export),
            ]
        return new_urls + urls

    #CSV Querry
    def export(self, request):
        if request.user.is_superuser:

            response = HttpResponse(content_type='text/csv')
            writer = csv.writer(response, quoting=csv.QUOTE_NONE, delimiter='|', quotechar=None ,escapechar='\\')
            writer.writerow (['Category', 'Source ','Promotion', 'Author', 'Title', 'Content', 'Date Posted', 'Youtube URL', 'Tiktok URL', 'Insta URL'])

            for movie in Movie.objects.all().values_list('category', 'source', 'promotion', 'author', 'title', 'content', 'date_posted', 'youtube_url', 'tiktok_url', 'insta_url'):
                writer.writerow(movie)
        
            response['Content-Disposition'] = 'attachement; filename="movies.txt"'
      
            return response
        else:
            return redirect('page-home')


    #views for CSV download page  
    def download_csv(self, request):
        if request.user.is_superuser:
            return render(request, 'admin/csv_download.html')
        else:
            return redirect('page-home')


    #views for CSV upload page
    def upload_csv(self, request):
        if request.user.is_superuser:
            if request.method == 'POST':
                csv_file = request.FILES["csv_upload"]
                file_data = csv_file.read().decode('utf-8')
                csv_data = file_data.split("\n")
                try:
                    for x in csv_data:
                        fields = x.split("|")
                        if x:    
                        #example file movies_example_upload_file.txt set as "|" delimited in main project directory
                            Movie.objects.update_or_create(
                                    category = fields[0],
                                    source = fields[1],
                                    promotion = fields[2],
                                    author = fields[3],
                                    title = fields[4],
                                    content = fields[5],
                                    date_posted=fields[6],
                                    youtube_url = fields[7],
                                    tiktok_url = fields[8],
                                    insta_url = fields[9],
                                
                            )
                    messages.success(request, f'Dane zostały wgrane do bazy danych!')                                       
                except Exception:
                     messages.warning(request, f'Uwaga: Błędne formatowanie zawartości pliku, popraw plik i wgraj ponownie!')

            form = ImportCsvForm()
            data = {"form": form}
            
            
            return render(request, 'admin/csv_upload.html', data)
            
        
        else:
            return redirect('page-home')



    @admin.action(description='Dodaj do promowanych')
    def make_promotion(self, request, queryset):
         updated = queryset.update(promotion=True)
         self.message_user(request, ngettext(
            '%d Wybrany film został dodany do promowanych',
            '%d Wybrane filmy zostały dodane do promowanych.',
            updated,
        ) % updated, messages.SUCCESS)

    @admin.action(description='Usuń z promowanych')
    def cancel_promotion(self, request, queryset):
        updated = queryset.update(promotion=False)
        self.message_user(request, ngettext(
            '%d Wybrany film został usunięty z promowanych',
            '%d Wybrane filmy zostały usunięte z promowanych.',
            updated,
        ) % updated, messages.SUCCESS)


# Register your models here.
admin.site.register(Movie, MovieAdmin)
admin.site.register(IpModel)
admin.site.register(Post)

