from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import Http404

# Create your views here.
@method_decorator(login_required,name='dispatch')
class ThreadList(TemplateView):
    # momdel = Thread
    template_name = 'messanger/thread_list.html'



@method_decorator(login_required,name='dispatch')
class ThreadDetail(DetailView):
    model = Thread

    #this is to make sure that the user cannot access a thread he does not belong to
    def get_object(self):
        obj = super(ThreadDetail,self).get_object()
        if self.request.user not in obj.objects.all():
            raise Http404
        return obj