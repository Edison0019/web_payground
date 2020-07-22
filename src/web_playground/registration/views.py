from .forms import FormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
class SignUpView(CreateView):
    form_class = FormWithEmail
    template_name ='registration/signup.html'
    def get_success_url(self):
        return reverse_lazy('login') + '?register'
    def get_form(self,form_class=None):
        form = super(SignUpView,self).get_form()
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2','placeholder':'Enter user name'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb-2','placeholder':'Enter email here'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Password'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2','placeholder':'Repeat password'})
        return form


@method_decorator(login_required,name='dispatch')
class CreateProfile(UpdateView):
    template_name = 'registration/profile_form.html'
    model = Profile
    fields =['avatar','bio','link']
    success_url = reverse_lazy('profile')

    def get_object(self):
        #getting the request from the user in order to 
        profile, created =  Profile.objects.get_or_create(user=self.request.user)
        return profile