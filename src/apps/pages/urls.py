from django.urls import path
from . import views
from .views import (
    LifestyleView, 
    MoviesView, 
    HotTopView, 
    OdkryciaView, 
    BeautyView, 
    FunnyView, 
    LifestyleView, 
    GamingView, 
    SportView)


urlpatterns = [
    path('', MoviesView.as_view(), name='page-home'),
    path('hot-top/', HotTopView.as_view(), name='page-hot_top'),
    path('odkrycia/', OdkryciaView.as_view(), name='page-odkrycia'),
    path('beauty/', BeautyView.as_view(), name='page-beauty'),
    path('funny/', FunnyView.as_view(), name='page-funny'),
    path('lifestyle/', LifestyleView.as_view(), name='page-lifestyle'),
    path('gaming/', GamingView.as_view(), name='page-gaming'),
    path('sport/', SportView.as_view(), name='page-sport'),
]

