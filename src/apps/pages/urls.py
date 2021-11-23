from django.urls import path
from . import views
from .views import MoviesView, HotTopView, OdkryciaView, BeautyView


urlpatterns = [
    path('', MoviesView.as_view(), name='page-home'),
    path('hot-top/', HotTopView.as_view(), name='page-hot_top'),
    path('odkrycia/', OdkryciaView.as_view(), name='page-odkrycia'),
    path('beauty/', BeautyView.as_view(), name='page-beauty'),
]

