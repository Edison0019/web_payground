from django.urls import path
from .views import ProfileDetail, ProfileList

urlpatterns = [
    path('',ProfileList.as_view(),name='profile_list'),
    path('<username>/',ProfileDetail.as_view(),name='profile_detail'),
]
