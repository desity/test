"""testproject URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from testapp import views

urlpatterns = [
    url(r'^testlist/$', views.test_list, name='test_list'),
    #(r'^thankyou/(?P<pk>[0-9]+)/$', views, name='thankyou'),
    # url(r'^test/(?P<pk>[0-9]+)/$quest/(?P<pk>[0-9]+)/$', views.question_list, name='question_list'),
    url(r'^test/(?P<pk>[0-9]+)/$', views.question_list, name='question_list'),# quest - вказується в формуванні посилань в test_list
    url(r'^submit/$', views.submit),
    url(r'^$', views.home, name='home'),
    url(r'^$', views.logout, name='logout'),


]
