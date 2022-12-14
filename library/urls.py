"""library URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from django.contrib import admin
from django.contrib.auth import views 
from libman import views as core_views
from django.views.generic import RedirectView
#from django.contrib.auth.views.LoginView

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', core_views.redir, name='redirect_view'),
    re_path(r'^login/$', views.LoginView.as_view(), name='login'),
    re_path(r'^logout/$', views.LogoutView.as_view(), {'next_page': '/login/'}, name='logout'),
    re_path(r'^signup/$', core_views.signup, name='signup'),
    re_path(r'^library/', include('libman.urls')),
]
