from django.urls import path
from . import views
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path("education/", views.education_certifications, name="education"),
    path('contact/', views.contact, name='contact'),
    path("favicon.ico",RedirectView.as_view(url=staticfiles_storage.url("image/favicon.ico"), permanent=True),),]
