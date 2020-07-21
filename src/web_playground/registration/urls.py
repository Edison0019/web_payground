from django.urls import path
from .views import SignUpView, CreateProfile

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('profile/',CreateProfile.as_view(),name='profile')
]
