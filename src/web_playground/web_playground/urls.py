"""web_playground URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from pages.urls import pages_patterns
from django.conf import settings

urlpatterns = [
    #core views
    path('',include('core.urls')),

    #pages views
    path('pages/',include(pages_patterns)),

    #admin path [default]
    path('admin/', admin.site.urls),

    #path del auth [for the registration/login page] for the registration app
    path('accounts/',include('django.contrib.auth.urls')),

    #url pattern for the registration app
    path('accounts/',include('registration.urls')),

    #profiles app
    path('profiles/',include('profiles.urls')),

    #profiles app
    path('messages/',include('messanger.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)