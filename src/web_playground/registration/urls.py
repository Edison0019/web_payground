from django.urls import path
from .views import SignUpView, CreateProfile, UpdateEmailView

urlpatterns = [
    path('signup/',SignUpView.as_view(),name='signup'),
    path('profile/',CreateProfile.as_view(),name='profile'),
    path('profile/email',UpdateEmailView.as_view(),name='profile_email')
]
