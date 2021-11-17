from django.urls import path
from . import views
from .views import MoviesView, HotTopView


urlpatterns = [
    path('', MoviesView.as_view(), name='page-home'),
    path('hot-top/', HotTopView.as_view(), name='page-hot')
]

