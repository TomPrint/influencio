from typing import Text
import django_filters
from django.forms.widgets import TextInput

from .models import * # gwiazdka importuje wszystkie modele

class MovieFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(label='', lookup_expr='contains',  widget=TextInput(attrs={'placeholder': 'Szukaj po nazwie'}))
    
    class Meta:
        model = Movie
        fields = ['author',]
