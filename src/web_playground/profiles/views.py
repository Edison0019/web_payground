from django.shortcuts import render
from django.views.generic import ListView, DetailView
from registration.models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.

class ProfileList(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        # this method is for returning the a field of a one to one relationship
        return get_object_or_404(Profile, user__username=self.kwargs['username'])