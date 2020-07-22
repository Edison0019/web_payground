from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class FormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.SlugField(required=True,help_text='')

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already registered, please try another one')
        return email

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar','bio','link']
        widgets = {
            'avatar' : forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'bio' : forms.Textarea(attrs={'class':'form-control','placeholder':'Enter bio here','rows':3}),
            'link' : forms.TextInput(attrs={'class':'form-control','placeholder':'write link here'})
        }
    