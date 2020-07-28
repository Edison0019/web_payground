from django.shortcuts import render
from django.views.generic import ListView, DetailView
from registration.models import Profile
from django.shortcuts import get_object_or_404
# Create your views here.

class ProfileList(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    #this attribute allows us to use pagination in django by assigning the number of
    #instances to be returned per each page as below
    paginate_by = 4

class ProfileDetail(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        # this method is for returning the a field of a one to one relationship
        return get_object_or_404(Profile, user__username=self.kwargs['username'])