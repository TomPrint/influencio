from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from .models import Movie

class ImportCsvForm(forms.Form):
    list_display = forms.FileField()

class MovieAdmin(admin.ModelAdmin):
    list_display = ('author','title','category','source','promotion','date_posted')
    #admin filter
    list_filter = ('author', 'title', )
    #admin search
    search_fields = ['author', 'title',]

    def get_urls(self):
        urls = super().get_urls()
        new_urls = [
            path('upload-csv/', self.upload_csv),
            ]
        return new_urls + urls

    def upload_csv(self, request):
        #test for post from form
        if request.method == 'POST':
            print("action is post")


        form = ImportCsvForm()
        data = {"form": form}
        return render(request, 'admin/csv_upload.html', data)





# Register your models here.
admin.site.register(Movie, MovieAdmin)

