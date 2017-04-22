"""mypro URL Configuration

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
from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
	
	url(r'^$', 'maid.views.home'),#, name='homepages'),
    url(r'^homemaid/', 'maid.views.homemaid'),
    url(r'^aboutus/', 'maid.views.about'),
    url(r'^homeclient/', 'maid.views.homeclient'),
    url(r'^maid/', 'maid.views.maid_reg'),
    url(r'^client/', 'maid.views.client_reg'),
    url(r'^maidlogin/', 'maid.views.maid_login'),
    url(r'^availability/', 'maid.views.availability'),
    url(r'^clientlogin/', 'maid.views.client_login'),
    url(r'^search/', 'maid.views.search'),
    url(r'^results/', 'maid.views.results'),
    url(r'^delete/', 'maid.views.delete'),


    url(r'^admin/', include(admin.site.urls)),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
