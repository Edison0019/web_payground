from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Thread,Message
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView
from django.http import Http404,JsonResponse
from django.shortcuts import get_object_or_404

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
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request,pk):
    response = {'created':'False'}
    if request.user.is_authenticated:
        #THIS IS TO RETURN THE DICTIONARY IN THE GET REQUEST and also the get method to access a particular key
        content = request.GET.get('content')
        if content:
            thread = get_object_or_404(Thread,pk=pk)
            message = Message.objects.create(content=content,user=request.user)
            #this part here is for adding the message to the thread
            thread.message.add(message)
            response['created'] = 'True'
    else:
        raise Http404('User not authenticated')
    return JsonResponse(response,safe=False)