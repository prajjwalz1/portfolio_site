from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import  re_path
urlpatterns = [
    path('', views.home, name='home'),
    path('', views.send_email, name='send_email'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    re_path(r'^send-email/$', views.send_email, name='send_email'),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
