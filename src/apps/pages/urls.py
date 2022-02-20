from django.urls import path
from . import views
from .views import (
    LifestyleView, 
    MoviesView,
    MixView,  
    BeautyView, 
    FunnyView, 
    LifestyleView, 
    GamingView, 
    SportView,
    TravelView,
    SztukaView,
    CreatorsView,
    ArticlesListView,
    )


urlpatterns = [
    path('', MoviesView.as_view(), name='page-home'),
    path('travel/', TravelView.as_view(), name='page-travel'),
    path('mix/', MixView.as_view(), name='page-mix'),
    path('sztuka/', SztukaView.as_view(), name='page-sztuka'),
    path('beauty/', BeautyView.as_view(), name='page-beauty'),
    path('funny/', FunnyView.as_view(), name='page-funny'),
    path('lifestyle/', LifestyleView.as_view(), name='page-lifestyle'),
    path('gaming/', GamingView.as_view(), name='page-gaming'),
    path('sport/', SportView.as_view(), name='page-sport'),
    path('creators/', CreatorsView.as_view(), name='page-creators'),
    path('kontakt/',  views.contact, name='page-contact'),
    path('privacy/',  views.privacy, name='page-privacy'),
    path('about/',  views.about, name='page-about'),
    path('articles/', ArticlesListView.as_view(), name='page-articles'),
]

