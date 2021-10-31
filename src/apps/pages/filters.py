import django_filters

from .models import * # gwiazdka importuje wszystkie modele

class MovieFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(label='Wyszukaj film po nazwie:',lookup_expr='contains')  
    
    class Meta:
        model = Movie
        fields = ['title']