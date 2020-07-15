from django.urls import path
from .views import sample,home

urlpatterns = [
    path('', home.as_view(), name="home"),
    path('sample/', sample.as_view(), name="sample"),
]