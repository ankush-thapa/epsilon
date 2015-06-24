"""rottenouttips URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.views.decorators.cache import cache_page
from django.views.generic import TemplateView
from django.conf.urls import include, url 
from django.contrib import admin
from . import views

urlpatterns = [ 
    url(r'^$', views.homepage , name='homepage'),
    url(r'^about/$', cache_page(1)(TemplateView.as_view(template_name='about.html')), name='about'),
    url(r'^contact/$', cache_page(1)(TemplateView.as_view(template_name='contact.html')), name='contact'),
    url(r'^contact-me/$', views.contact_me, name="contact"),
    url(r'^blog/(?P<slug>[-\w]+)/$', views.blog_page, name='about'),
    url(r'^category/(?P<category>[-\w]+)/(?P<category_id>[-\w]+)/$', views.category_page, name='category-page')
]
