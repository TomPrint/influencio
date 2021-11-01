import django_filters

from .models import * # gwiazdka importuje wszystkie modele

class MovieFilter(django_filters.FilterSet):
    author = django_filters.CharFilter(label='Wyszukaj film po nazwie influencera',lookup_expr='contains')  
    
    class Meta:
        model = Movie
        fields = ['author']