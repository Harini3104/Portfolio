from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('projects/', views.projects, name='projects'),
    path("education/", views.education_certifications, name="education"),
    path('contact/', views.contact, name='contact'),
]
