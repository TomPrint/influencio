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

##################### CLASS - BASED VIEWS #####################

#Home View - all movies without category filter
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
        context['submitButton'] = 'Szukaj'
        return context

#Hot-Top View
class HotTopView (FilterView):
    model = Movie
    template_name = 'pages/hot_top.html'
    filterset_class = MovieFilter 
    paginate_by = 6

    # query_set for dajango-filter with category filter
    def get_queryset(self):
        category_qs = self.model.objects.filter(category="HOT-TOP")
        return category_qs.order_by('-date_posted')

    # pass a context=label for submit Button that search movies in chosen category
    def get_context_data(self, **kwargs):
        context = super(HotTopView, self).get_context_data(**kwargs)
        context['submitButton'] = 'Szukaj w Hot-Top'
        return context

#Odkrycia View
class OdkryciaView (FilterView):
    model = Movie
    template_name = 'pages/odkrycia.html'
    filterset_class = MovieFilter
    paginate_by = 6

    # query_set for dajango-filter with category filter
    def get_queryset(self):
        category_qs = self.model.objects.filter(category="ODKRYCIA")
        return category_qs.order_by('-date_posted')
    
    # pass a context=label for submit Button that search movies in chosen category
    def get_context_data(self, **kwargs):
        context = super(OdkryciaView, self).get_context_data(**kwargs)
        context['submitButton'] = 'Szukaj w Odkrycia'
        return context

#Beauty View
class BeautyView (FilterView):
    model = Movie
    template_name = 'pages/beauty.html'
    filterset_class = MovieFilter
    paginate_by = 6
    
    # query_set for dajango-filter with category filter
    def get_queryset(self):
        category_qs = self.model.objects.filter(category="BEAUTY")
        return category_qs.order_by('-date_posted')
    
    # pass a context=label for submit Button that search movies in chosen category
    def get_context_data(self, **kwargs):
        context = super(BeautyView, self).get_context_data(**kwargs)
        context['submitButton'] = 'Szukaj w Beauty'
        return context

#Funny View
class FunnyView (FilterView):
    model = Movie
    template_name = 'pages/funny.html'
    filterset_class = MovieFilter
    paginate_by = 6
    
    # query_set for dajango-filter with category filter
    def get_queryset(self):
        category_qs = self.model.objects.filter(category="ŚMIESZNE")
        return category_qs.order_by('-date_posted')
    
    # pass a context=label for submit Button that search movies in chosen category
    def get_context_data(self, **kwargs):
        context = super(FunnyView, self).get_context_data(**kwargs)
        context['submitButton'] = 'Szukaj w Śmieszne'
        return context
        
#Gamming View
class GamingView (FilterView):
    model = Movie
    template_name = 'pages/lifestyle.html'
    filterset_class = MovieFilter
    paginate_by = 6
    
    # query_set for dajango-filter with category filter
    def get_queryset(self):
        category_qs = self.model.objects.filter(category="LIFESTYLE")
        return category_qs.order_by('-date_posted')

    # pass a context=label for submit Button that search movies in chosen category
    def get_context_data(self, **kwargs):
        context = super(GamingView, self).get_context_data(**kwargs)
        context['submitButton'] = 'Szukaj w Gaming'
        return context

#Lifestyle View
class LifestyleView (FilterView):
    model = Movie
    template_name = 'pages/lifestyle.html'
    filterset_class = MovieFilter
    paginate_by = 6
    
    # query_set for dajango-filter with category filter
    def get_queryset(self):
        category_qs = self.model.objects.filter(category="LIFESTYLE")
        return category_qs.order_by('-date_posted')

    # pass a context=label for submit Button that search movies in chosen category
    def get_context_data(self, **kwargs):
        context = super(LifestyleView, self).get_context_data(**kwargs)
        context['submitButton'] = 'Szukaj w Lifestyle'
        return context

#Sport View
class SportView (FilterView):
    model = Movie
    template_name = 'pages/sport.html'
    filterset_class = MovieFilter
    paginate_by = 6
    
   # query_set for dajango-filter with category filter 
    def get_queryset(self):
        category_qs = self.model.objects.filter(category="SPORT")
        return category_qs.order_by('-date_posted')

    # pass a context=label for submit Button that search movies in chosen category
    def get_context_data(self, **kwargs):
        context = super(SportView, self).get_context_data(**kwargs)
        context['submitButton'] = 'Szukaj w Sport'
        return context

##################### FUNCTION VIEWS #####################

def contact(request):
        context = {
            
      }
        return render (request,'pages/contact.html', context)
