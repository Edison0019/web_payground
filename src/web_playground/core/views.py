from django.shortcuts import render
from django.views.generic import TemplateView   


class home(TemplateView):
    template_name = 'core/home.html'

    def get(self,request,*args,**kwargs):
        return render(self.request,self.template_name,{'title':'My super web playground'})
    

class sample(TemplateView):
    template_name = 'core/sample.html'