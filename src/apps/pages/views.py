from django.shortcuts import render
from apps.pages.models import Movie
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django_filters.views import FilterView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import MovieFilter


# Create your views here.

# Admin Staff Mixin
class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff

class MoviesView (FilterView):
    model = Movie
    template_name = 'pages/home.html'
    filterset_class = MovieFilter
    paginate_by = 6
 
# query_set for dajango-filter
    def get_queryset(self):
        qs = self.model.objects.all()
        movie_filtered_list = MovieFilter(self.request.GET, queryset=qs)
        return movie_filtered_list.qs.order_by('-date_posted')

#pass new query_set to template to work with promotion zone apart from paginator and search field(django-filter)
    def get_context_data(self, **kwargs):
        context = super(MoviesView, self).get_context_data(**kwargs)
        context['movie_promotions'] = Movie.objects.all()
        return context


class HotTopView (FilterView):
    model = Movie
    template_name = 'pages/hot_top.html'
    filterset_class = MovieFilter
    
    paginate_by = 6

    def get_queryset(self):
        category_qs = self.model.objects.filter(category="HOT-TOP")
        return category_qs

class OdkryciaView (FilterView):
    model = Movie
    template_name = 'pages/odkrycia.html'
    filterset_class = MovieFilter
    paginate_by = 6


    def get_queryset(self):
        category_qs = self.model.objects.filter(category="ODKRYCIA")
        return category_qs

class BeautyView (FilterView):
    model = Movie
    template_name = 'pages/beauty.html'
    filterset_class = MovieFilter
    paginate_by = 6
    

    def get_queryset(self):
        category_qs = self.model.objects.filter(category="BEAUTY")
        return category_qs

