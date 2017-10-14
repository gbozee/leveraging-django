"""email_login URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.shortcuts import redirect, render
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views
from django.views.generic import FormView
from .forms import LoginForm

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


@views.login_required
def profile(request):
    return render(request, 'profile.html')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', LoginView.as_view(), name='login'),
    url(r'^accounts/profile/$',profile, name='profile'),
    url(r'^login/$', LoginView.as_view(), name='reg_login'),
    url('^', include('django.contrib.auth.urls')),
]
